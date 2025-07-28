from newclid import GeometricSolverBuilder, GeometricSolver
from newclid.statement import Statement
from newclid.formulations.definition import DefinitionJGEX
from newclid.dependencies.symbols import Point
from newclid.dependencies.dependency import Dependency, IN_PREMISES

from typing import Dict, List, Tuple, Union, Set
from datetime import datetime
from multiprocessing import Pool
from rich import print
import random
import json
import os
import re


AUXILIARY_CLAUSE_POLL  = [
    'midpoint',
    'angle_bisector',
    'on_bline',
    'on_pline',
    'on_tline',
    'psquare',
    'reflect',
    'parallelogram',
    'foot',
    'lc_tangent',
    'mirror',
    'nsquare',
    'shift',
    'incenter',
    'trisect',
    '3peq',
    'orthocenter',
    'centroid',
    'intersection_ll',
    'intersection_lp',
    'intersection_lt',
    'intersection_pp'
]


def statement_fl(statement: Statement) -> str:
    res = statement.predicate.NAME + ' '
    for a in statement.args:
        a_str = repr(a)
        if 'Fraction' in a_str:
            match = re.match(r"Fraction\((\d+),\s*(\d+)\)", a_str)
            if match:
                numerator = match.group(1) 
                denominator = match.group(2) 
                a_str = f'{numerator}/{denominator}'
        res += a_str + " "
    return res


def get_suitable_new_points(
    ori_points_names: List[str], new_points_num: int
) -> List[str]:
    if 26 - len(ori_points_names) < new_points_num:
        return None # type: ignore
    all_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    remaining_letters = [
        letter for letter in all_letters if letter not in ori_points_names
        ]
    return remaining_letters[:new_points_num]


def get_place_holder_str(points_names_list: List[str]) -> str:
    return ' '.join(['{' + pn + '}' for pn in points_names_list])


def get_cla_format_infos(cla_ins: DefinitionJGEX):
    cla_name = cla_ins.declare[0]
    cla_points_names = cla_ins.declare[1:]
    rely_points_names = cla_ins.rely.keys()
    input_vars: List[str] = []
    output_vars: List[str] = []
    for pn in cla_points_names:
        if pn in rely_points_names:
            output_vars.append(pn)
        else:
            input_vars.append(pn)

    former_place_holder_str = ' '.join(['{' + pn + '}' for pn in output_vars])
    latter_place_holder_str = ' '.join(['{' + pn + '}' for pn in cla_points_names])
    format_str = former_place_holder_str + ' = ' + cla_name + ' ' + latter_place_holder_str
    return {
        "input_vars": input_vars,
        "output_vars": output_vars,
        "format_str": format_str
    }


def map_place_holder_points(
    cla_format_infos: Dict[str, Union[List[str], str]],
    input_points_names: List[str],
    output_points_name: List[str]
) -> str:
    input_vars = cla_format_infos['input_vars']
    output_vars = cla_format_infos['output_vars']
    format_str = cla_format_infos['format_str']

    points_names_map: Dict[str, str] = {}
    for i in range(len(input_vars)):
        points_names_map[input_vars[i]] = input_points_names[i]

    for j in range(len(output_vars)):
        points_names_map[output_vars[j]] = output_points_name[j]

    cla_str = format_str.format(**points_names_map) # type: ignore
    return cla_str


def caption_build(c_str: str) -> GeometricSolver:
    try:
        solver_builder = GeometricSolverBuilder(1234)
        solver_builder.load_problem_from_txt(c_str)
        solver = solver_builder.build()
        return solver
    except Exception as e:
        return # type: ignore


def picking_clause(
    solver: GeometricSolver, 
    ori_all_points_names: List[str],
    c_str_ori: str,
    max_steps: int = 10
) -> Tuple[str, GeometricSolver]:
    psteps = 0
    while True:
        cla_name = random.choice(AUXILIARY_CLAUSE_POLL)
        cla_ins = solver.proof.defs[cla_name]
        needed_points_num = len(cla_ins.require.points)
        if needed_points_num <= len(ori_all_points_names):
            cla_format_infos = get_cla_format_infos(cla_ins)
            input_points_names = random.sample(
                ori_all_points_names, needed_points_num
            )
            output_points_names = get_suitable_new_points(
                ori_all_points_names, len(cla_ins.rely)
            )
            cla_str = map_place_holder_points(
                cla_format_infos, input_points_names, output_points_names
            )

            c_str_new = c_str_ori + '; ' + cla_str
            new_solver = caption_build(c_str_new)
            if new_solver:
                return c_str_new, new_solver

        psteps += 1
        if psteps >= max_steps:
            print(f'can not sample auxiliary points within the {max_steps} steps')
            return # type: ignore


def get_all_premises(
    hyper_graph: dict[Statement, Dependency]
) -> Set[Dependency]:
    res: Set[Dependency] = set()
    for _, dep in hyper_graph.items():
        if dep.reason == IN_PREMISES:
            res.add(dep)

    return res


def statement_fl(statement: Statement) -> str:
    res = statement.predicate.NAME + ' '
    for a in statement.args:
        res += repr(a) + " "
    return res


def check_aux_statement_solving(
    ori_c_str: str,
    aux_statement: Statement
) -> bool:
    # Due to the fact that ar is a triggering mechanism when solving newclid, 
    # it is necessary to determine whether aux_statement can also be solved 
    # within the original caption.
    problem_str = ori_c_str + ' ? ' + statement_fl(aux_statement)
    problem_solver_builder = GeometricSolverBuilder(123)
    problem_solver_builder.load_problem_from_txt(problem_str)
    problem_solver = problem_solver_builder.build()

    res = problem_solver.run()
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    if res:
        print(f'[{formatted_time}] Aux solution checking: {problem_str}, Failed')
        return False
    else:
        print(f'[{formatted_time}] Aux solution checking: {problem_str}, Successful')
        return True


def add_auxiliary_point(c_str_ori: str, max_sample_cycles: int = 1000):
    ori_solver = caption_build(c_str_ori)
    if ori_solver:
        ori_all_points = ori_solver.proof.symbols_graph.nodes_of_type(Point)
        ori_all_points_names = [op.name for op in ori_all_points]

        sample_cycles = 0
        while sample_cycles <= max_sample_cycles:
            c_str_new, new_solver = picking_clause(ori_solver, ori_all_points_names, c_str_ori)
            
            ori_solver.run()
            new_solver.run()

            ori_statements: List[Statement] = ori_solver.proof.dep_graph.checked()
            new_statements: List[Statement] = new_solver.proof.dep_graph.checked()
            added_statements: List[Statement] = []
            for ns in new_statements:
                if ns not in ori_statements:
                    added_statements.append(ns)

            for ads in added_statements:
                ads_points_names = []
                for elem in ads.args:
                    if type(elem) == Point:
                        ads_points_names.append(elem.name)
                if all(elem in ori_all_points_names for elem in ads_points_names):
                    if check_aux_statement_solving(c_str_ori, ads):
                        return c_str_ori, c_str_new, ads

            sample_cycles += 1
        
        print('can not find a aux')
            
            
def process_caption(caption_str_ori: str, save_to: str):
    try:
        _, c_str_new, ads = add_auxiliary_point(caption_str_ori) # type: ignore
    except Exception as e:
        print(f'Error: Something went wrong when adding aux point. {e}')
        return

    write_data = {
        "ori_caption": caption_str_ori,
        'new_caption': c_str_new,
        "target_statement": statement_fl(ads)
    }

    with open(save_to, 'w', encoding='utf-8') as wf:
        json.dump(write_data, wf, ensure_ascii=False, indent=4)



if __name__ == '__main__':
    caption_str_ori = 'a b c d = trapezoid a b c d; c a b = r_triangle c a b; d a b =r_triangle d a b ? rconst a c b d 1'
    save_to = './outputs/aux_point().json'
    process_caption(caption_str_ori, save_to)
