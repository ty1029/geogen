from newclid.statement import Statement
from newclid.proof import ProofState
from newclid.dependencies.symbols import Point, Line, Circle
from newclid.numerical.geometries import (
    PointNum,
    intersect,
)

from matplotlib.axes import Axes
from matplotlib.figure import Figure
import matplotlib.patches as patches
from typing import List, Dict, Any, Optional, Tuple


from drawing_completor import DrawingCompletor


def init_figure() -> "Figure":
    imsize = 1024 / 100
    fig = Figure(figsize=(imsize, imsize))
    ax = fig.add_subplot(111)  # type: ignore
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=0, hspace=0)
    ax.set_facecolor((1, 1, 1))
    ax.set_aspect("equal", adjustable="datalim")
    return fig


def fill_missing(d0: Dict[Any, Any], d1: Dict[Any, Any]):
    for k in d1.keys():
        if k not in d0:
            d0[k] = d1[k]


def draw_circle(ax: "Axes", c: Circle, **args: Any) -> None:
    fill_missing(
        args,
        {
            "color": "black",
            "fill": False,
            "lw": 2.0,
            "alpha": 0.9
        },
    )
    ax.add_patch(
        patches.Circle(  # type: ignore
            (c.num.center.x, c.num.center.y), c.num.radius, **args
        )
    )


def draw_line(ax: "Axes", line: Line, **args: Any):
    """Draw a line. Return the two extremities"""
    fill_missing(args, {"color": "black", "lw": 2.0, "alpha": 0.9})

    points: list[PointNum] = [p.num for p in line.points]
    p0, p1 = points[:2]
    # ax.axline((p0.x, p0.y), (p1.x, p1.y), **args)  # type: ignore
    ax.plot((p0.x, p1.x), (p0.y, p1.y), **args)


def draw_point(
    ax: "Axes",
    p: Point,
    args_point: Optional[dict[Any, Any]] = None,
    args_name: Optional[dict[Any, Any]] = None,
) -> None:
    """draw a point."""
    args_point = args_point or {}
    args_name = args_name or {}
    fill_missing(args_point, {"color": "black", "s": 5.0})
    ax.scatter(p.num.x, p.num.y, **args_point)  # type: ignore
    fill_missing(args_name, {
        "color": "black", 
        "fontsize": 12,
        "xytext": (5, 5),
        "textcoords": 'offset points', 
        "bbox": dict(
            facecolor='white',
            edgecolor='none',
            alpha=0.7,
            pad=0.1 
        )
    })
    ax.annotate(  # type: ignore
        p.pretty_name, (p.num.x, p.num.y), **args_name
    )


def draw_figure(cstr: str, proof: ProofState, save_to: str):
    symbols_graph = proof.symbols_graph
    points: List[Point] = list(symbols_graph.nodes_of_type(Point))
    lines: List[Line] = list(symbols_graph.nodes_of_type(Line))
    circles: List[Circle] = list(symbols_graph.nodes_of_type(Circle))

    points_dict: Dict[str, Point] = {}

    fig = init_figure()
    (ax, ) = fig.axes

    for p in points:
        draw_point(ax, p)
        points_dict[p.name] = p

    for l in lines:
        draw_line(ax, l)

    for c in circles:
        draw_circle(ax, c)

    draw_completor = DrawingCompletor(cstr, points_dict, ax)
    draw_completor.complete()

    fig.savefig(save_to) 
