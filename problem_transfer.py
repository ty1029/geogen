import re
import os
import json
import sqlite3
from rich import print
from collections import Counter
from def_description import DEF_DESCRIPTION

# 定义一个函数来提取形式化语言中的点，并生成对应描述
def des_generator(formal_language: str) -> str:
    # 正则表达式检查形式化语言的模式
    pattern = r"(\w+)\s+([\w\s]+)"  # 提取 "函数名" 和 "参数列表"
    match = re.match(pattern, formal_language)

    if not match:
        raise ValueError("Invalid formal language format provided")
    
    # 提取函数名和参数
    function_name, params_str = match.groups()
    params = params_str.split()  # 按空格拆分参数列表

    # 验证函数名是否在描述映射中
    if function_name not in DEF_DESCRIPTION:
        raise ValueError(f"Function '{function_name}' is not defined in descriptions")

    # 获取输入参数的顺序以及对应的描述模板
    entry = DEF_DESCRIPTION[function_name]
    input_order = entry["input"]
    description_template = entry["description"]

    if len(input_order) != len(params):
        raise ValueError(f"Function '{function_name}' expects {len(input_order)} parameters, but got {len(params)}")

    # 构造参数字典，将输入的点转为大写，按输入顺序映射
    param_dict = {input_order[i]: params[i].upper() for i in range(len(params))}

    # 返回格式化后的描述
    return description_template.format(**param_dict)


def parse_formal_language(text):
    # 使用 '?' split，将问题描述和问题分开
    description, problem = text.split('?')
    
    # 分别用 ';' split，将每条形式化语言分开
    description_parts = [part.strip() for part in description.split(';') if part.strip()]
    problem_parts = [part.strip() for part in problem.split(';') if part.strip()]
    
    # 返回两个 tuple，分别存储问题描述和问题
    return tuple(description_parts), tuple(problem_parts)


def get_problem_data(db_path: str):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(
        """SELECT id, problem_FL FROM proofs WHERE problem_pretty IS NULL;"""
    )
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


def process_cap_element(string_tuple):
    results = []
    
    for string in string_tuple:

        if '=' in string:
            _, right_part = string.split('=', 1)
            right_part = right_part.strip()
            
            if ',' in right_part:
                sub_parts = [part.strip() for part in right_part.split(',')]
                results.extend(sub_parts)
            else:
                results.append(right_part)
    
    return results


def get_problem_pretty(problem_fl: str):
    try:
        caption_FL_list, problem_FL_list = parse_formal_language(problem_fl)
        cap_pretty = '\n'.join([des_generator(cap) for cap in process_cap_element(caption_FL_list)])
        prob_pretty = '\n'.join([des_generator(prob) for prob in problem_FL_list])
        problem_pretty = "# Description\n\n" + cap_pretty + '\n\n# Problem\n\n' + prob_pretty
        return problem_pretty
    except Exception as e:
        print(problem_fl + '(can not pretty)')


def get_max_step_label(input_string):
    """
    从输入的字符串中提取步骤标签，并返回数值最大的步骤标签。
    
    :param input_string: 输入的字符串
    :return: 最大的步骤标签（如 "039."），如果未找到返回 None
    """
    # 使用正则表达式匹配步骤标签，如 "039.", "004." 等
    step_labels = re.findall(r'\b(\d{3}\.)', input_string)
    
    if not step_labels:
        return None  # 如果没有找到步骤标签，返回 None
    
    # 提取出数值最大的步骤标签
    step_labels = [int(label.strip('.')) for label in step_labels]
    max_step_label = max(step_labels)
    
    return max_step_label + 1


def update_problem_pretty(db_path):
    # 获取所有需要更新的问题数据
    data = get_problem_data(db_path)
    print(f'{len(data)} problems need to be prettied.')

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    count = 0  # 用于计数当前已更新的数据条数
    
    for row in data:
        p_id, problem_FL = row
        try:
            # 生成 `problem_pretty` 的内容
            caption_FL_list, problem_FL_list = parse_formal_language(problem_FL)
            cap_pretty = '\n'.join([des_generator(cap) for cap in process_cap_element(caption_FL_list)])
            prob_pretty = '\n'.join([des_generator(prob) for prob in problem_FL_list])
            problem_pretty = "# Description\n\n" + cap_pretty + '\n\n# Problem\n\n' + prob_pretty
            
            # 更新数据库中的 `problem_pretty` 字段
            cur.execute(
                """UPDATE proofs SET problem_pretty = ? WHERE id = ?;""",
                (problem_pretty, p_id)
            )

            count += 1
            
            # 每 1000 条记录提交一次，以减少数据库操作压力
            if count % 1000 == 0:
                conn.commit()
                print(f"{count} rows have been committed.")
        
        except Exception as e:
            print(problem_FL)
            print(f"Error processing ID {p_id}: {e}")
            continue

    # 最后提交剩余未提交的更新
    conn.commit()
    print(f"All remaining updates committed. Total updates: {count}")
    
    # 关闭数据库连接
    cur.close()
    conn.close()



if __name__ == "__main__":
    # db_path = '/cpfs01/user/xiarenqiu/xiarenqiu/geo/think2geo/data/raw_geogen/final_filtered.db'
    # update_problem_pretty(db_path)

    bt_root_path = '/wuhu_uni_ai/geo/geo/think2geo/data/raw_geogen/backtrack_solutions'
    bt_update_path = '/wuhu_uni_ai/geo/geo/think2geo/data/raw_geogen/backtrack_solutions_update'
    problem_count = 0
    proof_length_list = []
    for fn in os.listdir(bt_root_path):
        if fn.endswith('.json'):
            fp = os.path.join(bt_root_path, fn)
            with open(fp, 'r', encoding='utf-8') as rf:
                json_data = json.load(rf)  
            output_json = {} 
            for pk, pv in json_data.items():
                output_json[pk] = []
                for elem in pv:
                    problem_fl = elem['problem_str']
                    solution_pretty = elem['traceback_solution_pretty']
                    problem_pretty = get_problem_pretty(problem_fl)
                    proof_length = get_max_step_label(solution_pretty)
                    output_json[pk].append(
                        {
                            "problem_fl": problem_fl,
                            "problem_pretty": problem_pretty,
                            "backtrack_solution_fl": elem['traceback_solution_raw'],
                            "backtrack_solution_pretty": elem['traceback_solution_pretty'],
                            "proof_length": proof_length,
                            "characters_nums": len(solution_pretty)
                        }
                    )
                    problem_count += 1 
                    proof_length_list.append(proof_length)
            output_path = os.path.join(bt_update_path, fn)
            with open(output_path, 'w', encoding='utf-8') as wf:
                json.dump(output_json, wf, ensure_ascii=False)


    print(problem_count)
    print(dict(Counter(proof_length_list)))