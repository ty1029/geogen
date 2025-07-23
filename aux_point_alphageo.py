# get aux problems by alphageo proposed algorithm

from newclid import GeometricSolverBuilder, GeometricSolver
from newclid.statement import Statement
from newclid.dependencies.symbols import Point

from typing import Dict, List, Union
from rich import print
import json
import re


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


def get_p_str_map(p_str: str) -> Dict[str, Dict]:
    p_str_map: Dict[str, Dict] = {}
    p_str_list = p_str.split(';')
    for i, construction in enumerate(p_str_list):
        if construction.startswith(' '):
            construction = construction[1:]
        cons_res, _ = construction.split('=')
        for point in cons_res.split(' '):
            if point:
                p_str_map[point] = {
                    'idx': i,
                    'construction': construction
                }
    return p_str_map


def constructions2p_str(constructions_list: List[Dict]):
    constructions_list.sort(key=lambda x: x['idx'])
    new_p_str = '; '.join([cons['construction'] for cons in constructions_list])
    return new_p_str


def constructions_are_sufficient(constructions_list: List[Dict]):
    new_p_str = constructions2p_str(constructions_list)
    try:
        solver_builder = GeometricSolverBuilder(1234)
        solver_builder.load_problem_from_txt(new_p_str)
        solver = solver_builder.build()
        return True
    except Exception as e:
        return False


def statement_is_aux(
    solver: GeometricSolver, s: Statement, p_str_map: Dict[str, Dict]
):
    statement_points = []
    for a in s.args:
        if isinstance(a, Point):
            if a.name not in statement_points:
                statement_points.append(a.name)
    proof_points = []
    proof_deps = solver.proof.dep_graph.proof_deps([s,])
    for dep in proof_deps:
        for condition in dep.why:
            for ca in condition.args:
                if isinstance(ca, Point):
                    if ca.name not in proof_points:
                        proof_points.append(ca.name)
        for sa in dep.statement.args:
            if isinstance(sa, Point):
                if sa.name not in proof_points:
                    proof_points.append(sa.name)

    statement_constructions = []
    proof_constructions = []
    
    for pp in proof_points:
        if p_str_map[pp] not in proof_constructions:
            proof_constructions.append(p_str_map[pp])
    
    for sp in statement_points:
        if p_str_map[sp] not in statement_constructions:
            statement_constructions.append(p_str_map[sp])

    aux_constructions = [
        cons for cons in proof_constructions if cons not in statement_constructions
    ]
    if aux_constructions:
        if constructions_are_sufficient(statement_constructions):
            original_problem = constructions2p_str(statement_constructions)
            full_problem = constructions2p_str(proof_constructions)
            return {
                'original_problem': original_problem,
                'full_problem': full_problem,
                'goal': statement_fl(s)
            }
        else:
            return


def process_caption(caption_str: str, save_to: str):
    try:
        solver_builder = GeometricSolverBuilder(1234)
        solver_builder.load_problem_from_txt(caption_str)
        solver = solver_builder.build()
    except Exception as e:
        return
    
    try:
        solver.run()
    except Exception as e:
        return

    checked_statement = solver.proof.dep_graph.checked()
    p_str_map = get_p_str_map(caption_str)
    aux_problems: Dict[str, Union[str, List]] = {
        "caption": caption_str,
        "auxiliary_problem": []
    }
    for i, s in enumerate(checked_statement):
        check_results = statement_is_aux(solver, s, p_str_map)
        if check_results:
            aux_problems['auxiliary_problem'].append(check_results) # type: ignore

    if aux_problems['auxiliary_problem']:
        with open(save_to, 'w', encoding='utf-8') as wf:
            json.dump(aux_problems, wf, ensure_ascii=False, indent=4)
        print(f"[green]find {len(aux_problems['auxiliary_problem'])} aux problems for[/green] {caption_str}")
    else:
        print(f'[red]no aux problem found for[/red] {caption_str}')



if __name__ == '__main__':
    caption_str = 'a = free a; b = lconst b a 18; c d = square a b c d; e f = trisect e f a b c; g = intersection_cc g b f c; h i j = ieq_triangle h i j'
    save_to = './outputs/aux_alphageo.json'
    process_caption(caption_str, save_to)