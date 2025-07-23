from newclid import GeometricSolverBuilder, GeometricSolver
from newclid.statement import Statement
from newclid.proof import ProofState
from newclid.dependencies.dependency import Dependency, IN_PREMISES, NUMERICAL_CHECK
from newclid.dependencies.symbols import Point
from rich import print
from typing import Dict, List, Union, Tuple, Set
import time
import os
import re
import json
from newclid.agent.ddarn import DDARN
from caption_draw import draw_figure

from problem_transfer import get_problem_pretty


def get_proof_steps(
    proof_state: "ProofState", problem_goals: List[Statement]
) -> Tuple[str, str, int, int, int]:
    id: dict[Statement, str] = {}
    goals = [goal for goal in problem_goals if goal.check()]
    for k, goal in enumerate(goals):
        id[goal] = f"g{k}"

    def rediger(dep: Dependency) -> str:
        for statement in (dep.statement,) + dep.why:
            if statement not in id:
                id[statement] = str(len(id) - len(goals))
        return f"{', '.join(premise.pretty() + ' [' + id[premise] + ']' for premise in dep.why)} ({dep.reason})=> {dep.statement.pretty()} [{id[dep.statement]}]"

    def rediger_raw(dep: Dependency) -> str:
        for statement in (dep.statement,) + dep.why:
            if statement not in id:
                id[statement] = str(len(id) - len(goals))
        return f"{', '.join(str(premise) + ' [' + id[premise] + ']' for premise in dep.why)} ({dep.reason})=> {str(dep.statement)} [{id[dep.statement]}]"

    def point_raw_name(point: Point) -> str:
        p = point.name[0].lower()
        for c in point.name[1:]:
            if c.isdigit():
                p += chr(ord("₀") + ord(c) - ord("0"))
            else:
                p += f"_{c}"
        return p

    solution = "==========================\n"
    solution += "* From problem construction:\n"
    solution += f"Points : {', '.join(p.pretty_name for p in proof_state.symbols_graph.nodes_of_type(Point))}\n"

    solution_raw = "==========================\n"
    solution_raw += "* From problem construction:\n"
    solution_raw += f"Points : {', '.join(point_raw_name(p) for p in proof_state.symbols_graph.nodes_of_type(Point))}\n"

    proof_deps = proof_state.dep_graph.proof_deps(goals)
    premises: list[Dependency] = []
    numercial_checked: list[Dependency] = []
    proof_steps: list[Dependency] = []

    for line in proof_deps:
        if IN_PREMISES == line.reason:
            premises.append(line)
        elif NUMERICAL_CHECK == line.reason:
            numercial_checked.append(line)
        else:
            proof_steps.append(line)

    for line in premises:
        solution += rediger(line) + "\n"
        solution_raw += rediger_raw(line) + '\n'
    for line in numercial_checked:
        solution += rediger(line) + "\n"
        solution_raw += rediger_raw(line) + '\n'
    solution += "* Proof steps:\n"
    solution_raw += "* Proof steps:\n"
    proof_length = 0
    for k, line in enumerate(proof_steps):
        if NUMERICAL_CHECK not in line.reason and IN_PREMISES not in line:
            solution += f"{k:03d}. {rediger(line)}\n"
            solution_raw += f"{k:03d}. {rediger_raw(line)}\n"
            
            proof_length += 1
    solution += "\n=========================="
    solution_raw += "\n=========================="

    premises_nums = len(premises)
    numerical_checked_nums = len(numercial_checked)

    return solution, solution_raw, proof_length, premises_nums, numerical_checked_nums


def get_all_premises(
    hyper_graph: dict[Statement, Dependency]
) -> Set[Dependency]:
    res: Set[Dependency] = set()
    for _, dep in hyper_graph.items():
        if dep.reason == IN_PREMISES:
            res.add(dep)

    return res


def get_all_numerical_checked(
    hyper_graph: dict[Statement, Dependency]
) -> Set[Dependency]:
    res: Set[Dependency] = set()
    for _, dep in hyper_graph.items():
        if dep.reason == NUMERICAL_CHECK:
            res.add(dep)

    return res


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


def caption2solution(caption_str, fig_path: str = '') -> Dict[str, Union[str, List]]:
    start = time.time()
    output_dict: Dict[str, Union[str, List]] = {
        "problems": []
    }
    caption_solver_builder = GeometricSolverBuilder(1234)
    caption_solver_builder.load_problem_from_txt(caption_str)
    caption_solver: GeometricSolver = caption_solver_builder.build()

    if fig_path:
        draw_figure(caption_str, caption_solver.proof, fig_path)

    caption_solver.run()

    all_premises = get_all_premises(
        caption_solver.proof.dep_graph.hyper_graph
    )
    all_numerical_checked = get_all_numerical_checked(
        caption_solver.proof.dep_graph.hyper_graph
    )
    all_premises_nums = len(all_premises)
    all_numerical_checked_nums = len(all_numerical_checked)

    for statement in caption_solver.proof.dep_graph.checked():
        solution_pretty, solution_raw, proof_length, premises_nums, numerical_checked_nums = get_proof_steps(
            caption_solver.proof, [statement,]
        )
        if proof_length >= 1:
            problem_str = caption_str + ' ? ' + statement_fl(statement)
            problem_pretty = get_problem_pretty(problem_str)

            output_dict['problems'].append(
                {
                    "problem_FL": problem_str,
                    "problem_pretty": problem_pretty,
                    "solution_FL": solution_raw,
                    "solution_pretty": solution_pretty,
                    "proof_length": proof_length,
                    "premises_nums": premises_nums,
                    "numerical_checked_nums": numerical_checked_nums,
                    "all_premises_nums": all_premises_nums,
                    "all_numerical_checked_nums": all_numerical_checked_nums
                }
            )

    end = time.time()
    output_dict['sample_cost'] = end - start

    return output_dict


if __name__ == '__main__':
    caption_str = 'a = free a; b = lconst b a 18; c = on_dia c a b; d = on_dia d a c; e f g h = cc_tangent e f g h b c d a'

    fig_save_path = './outputs/test_image.png'
    output_dict = caption2solution(caption_str, fig_path=fig_save_path)
    solution_save_path = './outputs/test_solution.json'
    with open(solution_save_path, 'w', encoding='utf-8') as wf:
        json.dump(output_dict, wf, ensure_ascii=False, indent=4)

