import re
import numpy as np
from typing import Dict, List
from matplotlib.axes import Axes
from matplotlib import pyplot as plt
from typing import Tuple, Any, Dict, List

from newclid.dependencies.symbols import Point


def fill_missing(d0: Dict[Any, Any], d1: Dict[Any, Any]):
    for k in d1.keys():
        if k not in d0:
            d0[k] = d1[k]


def plot_dash_line(point_a: Point, point_b: Point, ax: "Axes", **args: Any):
    fill_missing(args, {"color": "blue", "lw": 0.75, "alpha": 0.6, "linestyle": "--"})

    ax.plot(
        [point_a.num.x, point_b.num.x],
        [point_a.num.y, point_b.num.y],
        **args
    )


def plot_solid_line(point_a: Point, point_b: Point, ax: "Axes", **args: Any):
    fill_missing(args, {"color": "black", "lw": 2.0, "alpha": 0.9})

    ax.plot(
        [point_a.num.x, point_b.num.x],
        [point_a.num.y, point_b.num.y],
        **args
    )


def find_lconst_pattern(cstr: str) -> List[Tuple[str, str, int]]:
    pattern = r'lconst\s+(\w+)\s+(\w+)\s+(\d+)'
    
    results = []
    
    matches = re.finditer(pattern, cstr)

    for match in matches:
        c, b, num = match.groups()
        results.append((c, b, int(num)))
    
    return results


def draw_lconst(
    lconst_info_list: List[Tuple[str, str, int]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any
):
    fill_missing(args, {"color": "black", "lw": 2.0, "alpha": 0.9})
    
    for lconst_info in lconst_info_list:
        p1, p2, length = lconst_info
        p1 = points_dict.get(p1)
        p2 = points_dict.get(p2)
        ax.plot((p1.num.x, p2.num.x), (p1.num.y, p2.num.y), **args)

        # Calculate the midpoint coordinates of a line segment.
        mid_x = (p1.num.x + p2.num.x) / 2
        mid_y = (p1.num.y + p2.num.y) / 2
        
        # Calculate the offset (to prevent annotation from directly overlapping the line segment).
        dx = p2.num.x - p1.num.x
        dy = p2.num.y - p1.num.y
        length_vector = np.sqrt(dx**2 + dy**2)
        
        # Calculate the direction perpendicular to the line segment for offsetting.
        if length_vector != 0:
            offset_x = -dy / length_vector * 0.1  # 0.1 is the offset distance, adjustable as needed.
            offset_y = dx / length_vector * 0.1
        else:
            offset_x = offset_y = 0
            
        ax.text(
            mid_x + offset_x,
            mid_y + offset_y,
            str(length),
            ha='center',
            va='center',
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.7)
        )


def find_shift_patterns(cstr: str) -> List[Tuple[str, str, str, str]]:
    pattern = r'(\w+)\s*=\s*shift\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)'
    
    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        var1, var2, var3, var4, var5 = match.groups()
        if var1 == var2:
            results.append((var1, var3, var5, var4))

    return results


def draw_shift(
    shift_info_list: List[Tuple[str, str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any
):
    fill_missing(args, {"color": "black", "lw": 2.0, "alpha": 0.9})

    for shift_info in shift_info_list:
        p1, p2, p3, p4 = shift_info
        p1 = points_dict.get(p1)
        p2 = points_dict.get(p2)
        p3 = points_dict.get(p3)
        p4 = points_dict.get(p4)

    ax.plot((p1.num.x, p2.num.x), (p1.num.y, p2.num.y), **args)
    ax.plot((p3.num.x, p4.num.x), (p3.num.y, p4.num.y), **args)
    ax.plot((p2.num.x, p3.num.x), (p2.num.y, p3.num.y), **args)
    ax.plot((p1.num.x, p4.num.x), (p1.num.y, p4.num.y), **args)


def find_lc_tangent_patterns(cstr: str) -> List[Tuple[str, str, str]]:
    pattern = r'(\w+)\s*=\s*lc_tangent\s+(\w+)\s+(\w+)\s+(\w+)'
    
    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        var1, var2, var3, var4 = match.groups()
        if var1 == var2:
            results.append((var1, var3, var4))

    return results


def draw_lc_tangent(
    lc_tangent_info_list: List[Tuple[str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any
):
    fill_missing(
        args, {"color": "blue", "lw": 1.5, "alpha": 0.6, "linestyle": "-"}
        )
    for lc_tangent_info in lc_tangent_info_list:
        result_point, point_a, center_point = lc_tangent_info
        
        point_a = points_dict.get(point_a)
        center_point = points_dict.get(center_point)
        
        radius = np.sqrt(
            (point_a.num.x - center_point.num.x)**2 + 
                (point_a.num.y - center_point.num.y)**2
        )
        
        circle = plt.Circle(
            (center_point.num.x, center_point.num.y), 
            radius, 
            fill=False, 
            **args
        )
        
        ax.add_patch(circle)
        
        ax.plot(
            [center_point.num.x, point_a.num.x], 
            [center_point.num.y, point_a.num.y], 
            color=args["color"], 
            lw=args["lw"]/2, 
            alpha=args["alpha"],
            linestyle="--"
        )


def find_intersection_ll_patterns(
    cstr: str
) -> List[Tuple[str, str, str, str, str]]:
    pattern = r'(\w+)\s*=\s*intersection_ll\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)'
    
    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        var1, var2, var3, var4, var5, var6 = match.groups()
        if var1 == var2:
            results.append((var1, var3, var4, var5, var6))

    return results


def draw_intersection_ll(
    intersection_ll_info_list: List[Tuple[str, str, str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any
):
    for intersection_info in intersection_ll_info_list:
        _, c, a, o, b = intersection_info
        
        point_c = points_dict.get(c)
        point_a = points_dict.get(a)
        point_o = points_dict.get(o)
        point_b = points_dict.get(b)

        plot_solid_line(point_c, point_a, ax)
        plot_solid_line(point_o, point_b, ax)
        

def find_on_circle_patterns(cstr: str) -> List[Tuple[str, str, str]]:
    pattern = r'(\w+)\s*=\s*on_circle\s+(\w+)\s+(\w+)\s+(\w+)'
    
    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        var1, var2, var3, var4 = match.groups()
        results.append((var2, var3, var4))

    return results


def draw_on_circle(
    on_circle_info_list: List[Tuple[str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any
):
    fill_missing(
        args, {"color": "blue", "lw": 1.5, "alpha": 0.6, "linestyle": "-"}
    )
    for on_circle_info in on_circle_info_list:
        point_g, center_point_a, point_e = on_circle_info
        
        center_point_a = points_dict.get(center_point_a)
        point_e = points_dict.get(point_e)
        point_g = points_dict.get(point_g)
        
        radius = np.sqrt(
            (point_e.num.x - center_point_a.num.x)**2 + 
            (point_e.num.y - center_point_a.num.y)**2
        )
        
        circle = plt.Circle(
            (center_point_a.num.x, center_point_a.num.y), 
            radius, 
            fill=False, 
            **args
        )
        
        ax.add_patch(circle)

        plot_dash_line(center_point_a, point_e, ax, **args)
        plot_dash_line(center_point_a, point_g, ax, **args)


def find_ninepoints_patterns(cstr: str) -> List[Tuple[str, str, str, str, str, str, str]]:
    pattern = r'(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s*=\s*ninepoints\s+\w+\s+\w+\s+\w+\s+\w+\s+(\w+)\s+(\w+)\s+(\w+)'
    
    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        # 提取7个变量: l, m, n, p, g, b, h
        l, m, n, p, g, b, h = match.groups()
        results.append((l, m, n, p, g, b, h))

    return results


def draw_ninepoints(
    ninepoints_info_list: List[Tuple[str, str, str, str, str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any
):
    fill_missing(
        args, {"color": "blue", "lw": 1.5, "alpha": 0.6, "linestyle": "-"}
    )
    for ninepoints_info in ninepoints_info_list:
        l, m, n, p, g, b, h = ninepoints_info
        
        point_p = points_dict.get(p)
        point_l = points_dict.get(l)
        point_m = points_dict.get(m)
        point_n = points_dict.get(n)
        point_g = points_dict.get(g)
        point_b = points_dict.get(b)
        point_h = points_dict.get(h)

        radius = np.sqrt(
            (point_l.num.x - point_p.num.x)**2 + 
            (point_l.num.y - point_p.num.y)**2
        )

        circle = plt.Circle(
            (point_p.num.x, point_p.num.y),
            radius,
            fill=False,
            **args
        )
        ax.add_patch(circle)

        plot_solid_line(point_g, point_b, ax)
        plot_solid_line(point_g, point_h, ax)
        plot_solid_line(point_b, point_h, ax)

        plot_dash_line(point_p, point_l, ax)
        plot_dash_line(point_p, point_m, ax)
        plot_dash_line(point_p, point_n, ax)


def find_tangent_patterns(cstr: str) -> List[Tuple[str, str, str, str, str]]:
    pattern = r'(\w+)\s+(\w+)\s*=\s*tangent\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)'
    
    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        var1, var2, var3, var4, var5, var6, var7 = match.groups()
        if var1 == var3 and var2 == var4:
            results.append((var1, var2, var5, var6, var7))

    return results


def draw_tangent(
    tangent_info_list: List[Tuple[str, str, str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any
):
    fill_missing(
        args, {"color": "blue", "lw": 1.5, "alpha": 0.6, "linestyle": "-"}
    )
    
    for tangent_info in tangent_info_list:
        _, _, _, center, radius_point = tangent_info
        
        center_point = points_dict.get(center) 
        radius_point = points_dict.get(radius_point) 
        
        radius = np.sqrt(
            (radius_point.num.x - center_point.num.x)**2 + 
            (radius_point.num.y - center_point.num.y)**2
        )

        circle = plt.Circle(
            (center_point.num.x, center_point.num.y),
            radius,
            fill=False,
            **args
        )
        ax.add_patch(circle)

        plot_dash_line(center_point, radius_point, ax, **args)


def find_circle_patterns(cstr: str) -> List[Tuple[str, str, str]]:
    pattern = r'(\w+)\s*=\s*circle\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)'
    
    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        var1, var2, var3, var4, var5 = match.groups()
        results.append((var2, var3, var4, var5))

    return results


def find_circumcenter_patterns(cstr: str) -> List[Tuple[str, str, str]]:
    pattern = r'(\w+)\s*=\s*circumcenter\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)'
    
    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        var1, var2, var3, var4, var5 = match.groups()
        results.append((var2, var3, var4, var5))

    return results


def draw_circumcenter(
    circumcenter_info_list: List[Tuple[str, str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any  
):   # also used to draw circle
    fill_missing(args, {"color": "blue", "lw": 1.5, "alpha": 0.6, "linestyle": "-"})
    for circle_info in circumcenter_info_list:
        center, radius_point1, radius_point2, radius_point3 = circle_info
        
        center_point = points_dict.get(center)
        radius_points = [
            points_dict.get(radius_point1),
            points_dict.get(radius_point2),
            points_dict.get(radius_point3)
        ]
        
        radius = np.sqrt(
            (radius_points[0].num.x - center_point.num.x)**2 + 
            (radius_points[0].num.y - center_point.num.y)**2
        )
        
        circle = plt.Circle(
            (center_point.num.x, center_point.num.y),
            radius,
            fill=False,
            **args
        )
        ax.add_patch(circle)
        
        for radius_point in radius_points:
            plot_dash_line(center_point, radius_point, ax, **args)


def find_triangle_patterns(cstr: str) -> List[Tuple[str, str, str, str, str, str]]:
    pattern = r'(\w+)\s+(\w+)\s+(\w+)\s=\s*triangle\s+(\w+)\s+(\w+)\s+(\w+)'
    
    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        _, _, _, a, b, c = match.groups()
        results.append((a, b, c))

    return results


def draw_triangle(
    triangle_info_list: List[Tuple[str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any
):
    for triangle_info in triangle_info_list:
        a, b, c = triangle_info
        point_a = points_dict.get(a)
        point_b = points_dict.get(b)
        point_c = points_dict.get(c)

        plot_solid_line(point_a, point_b, ax)
        plot_solid_line(point_b, point_c, ax)
        plot_solid_line(point_c, point_a, ax)


def find_iso_triangle_vertex_patterns(cstr: str) -> List[Tuple[str, str, str]]:
    pattern = r'(\w+)\s*=\s*iso_triangle_vertex\s+(\w+)\s+(\w+)\s+(\w+)'
    
    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        var1, var2, var3, var4 = match.groups()
        results.append((var1, var2, var3, var4))

    return results


def draw_iso_triangle_vertex(
    iso_triangle_vertex_info_list: List[Tuple[str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any
):
    fill_missing(args, {"color": "black", "lw": 2.0, "alpha": 0.9})

    for iso_triangle_vertex_info in iso_triangle_vertex_info_list:
        _, a, b, c = iso_triangle_vertex_info
        point_a = points_dict.get(a)
        point_b = points_dict.get(b)
        point_c = points_dict.get(c)

        plot_solid_line(point_a, point_b, ax)
        plot_solid_line(point_b, point_c, ax)
        plot_solid_line(point_c, point_a, ax)


def find_parallelogram_patterns(cstr: str) -> List[Tuple[str, str, str, str, str]]:
    pattern = r'(\w+)\s*=\s*parallelogram\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)'
    
    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        _, a, b, c, d = match.groups()
        results.append((a, b, c, d))

    return results


def draw_parallelogram(
    parallelogram_info_list: List[Tuple[str, str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any
):
    fill_missing(args, {"color": "black", "lw": 2.0, "alpha": 0.9})

    for parallelogram_info in parallelogram_info_list:
        a, b, c, d = parallelogram_info
        point_a = points_dict.get(a)
        point_b = points_dict.get(b)
        point_c = points_dict.get(c)
        point_d = points_dict.get(d)

        plot_solid_line(point_a, point_b, ax)
        plot_solid_line(point_b, point_c, ax)
        plot_solid_line(point_c, point_d, ax)
        plot_solid_line(point_d, point_a, ax)


def find_centroid_patterns(cstr: str) -> List[Tuple[str, str, str]]:
    pattern = r'(\w+)\s+(\w+)\s+(\w+)\s=\s*centroid\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s(\w+)'
    
    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        _, _, _, a, b, c, d, e, f, g = match.groups()
        results.append((a, b, c, d, e, f, g))

    return results


def draw_centroid(
    centroid_info_list: List[Tuple[str, str, str, str, str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
):
    for centroid_info in centroid_info_list:
        a, b, c, d, e, f, g = centroid_info
        point_a = points_dict.get(a)
        point_b = points_dict.get(b)
        point_c = points_dict.get(c)
        point_d = points_dict.get(d)
        point_e = points_dict.get(e)
        point_f = points_dict.get(f)
        point_g = points_dict.get(g)

        plot_dash_line(point_d, point_a, ax)
        plot_dash_line(point_d, point_b, ax)
        plot_dash_line(point_d, point_c, ax)
        plot_dash_line(point_d, point_e, ax)
        plot_dash_line(point_d, point_f, ax)
        plot_dash_line(point_d, point_g, ax)  

        plot_solid_line(point_e, point_f, ax)
        plot_solid_line(point_f, point_g, ax)
        plot_solid_line(point_g, point_e, ax)    


def find_eqratio6_patterns(
    cstr: str
) -> List[Tuple[str, str, str, str, str, str, str]]:
    pattern = r'(\w+)\s=\s*eqratio6\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)'

    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        _, a, b, c, d, e, f, g = match.groups()
        results.append((a, b, c, d, e, f, g))   

    return results


def draw_eqratio6(
    eqratio6_info_list: List[Tuple[str, str, str, str, str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any
):
    for eqratio6_info in eqratio6_info_list:
        a, b, c, d, e, f, g = eqratio6_info
        point_a = points_dict.get(a)
        point_b = points_dict.get(b)
        point_c = points_dict.get(c)
        point_d = points_dict.get(d)
        point_e = points_dict.get(e)
        point_f = points_dict.get(f)
        point_g = points_dict.get(g)

        plot_dash_line(point_a, point_b, ax)
        plot_dash_line(point_a, point_c, ax)
        plot_dash_line(point_d, point_e, ax)
        plot_dash_line(point_f, point_g, ax)


def find_eqratio_patterns(
    cstr: str
) -> List[Tuple[str, str, str, str, str, str, str, str]]:
    pattern = r'(\w+)\s=\s*eqratio\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)'

    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        _, a, b, c, d, e, f, g, h = match.groups()
        results.append((a, b, c, d, e, f, g, h))   

    return results


def draw_eqratio(
    eqratio_info_list: List[Tuple[str, str, str, str, str, str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any
):
    for eqratio_info in eqratio_info_list:
        a, b, c, d, e, f, g, h = eqratio_info
        point_a = points_dict.get(a)
        point_b = points_dict.get(b)
        point_c = points_dict.get(c)
        point_d = points_dict.get(d)
        point_e = points_dict.get(e)
        point_f = points_dict.get(f)
        point_g = points_dict.get(g)
        point_h = points_dict.get(h)

        plot_dash_line(point_b, point_c, ax)
        plot_dash_line(point_d, point_e, ax)
        plot_dash_line(point_d, point_e, ax)
        plot_dash_line(point_f, point_g, ax)
        plot_dash_line(point_h, point_a, ax)


def find_eqdistance_patterns(cstr: str) -> List[Tuple[str, str, str, str]]:
    pattern = r'(\w+)\s*=\s*eqdistance\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)'
    
    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        _, var1, var2, var3, var4 = match.groups()
        results.append((var1, var2, var3, var4))

    return results


def draw_eqdistance(
    eqdistance_info_list: List[Tuple[str, str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any
):
    for eqdistance_info in eqdistance_info_list:
        a, b, c, d = eqdistance_info
        point_a = points_dict.get(a)
        point_b = points_dict.get(b)
        point_c = points_dict.get(c)
        point_d = points_dict.get(d)

        plot_dash_line(point_a, point_b, ax)
        plot_dash_line(point_c, point_d, ax)


def find_intersection_cc_patterns(cstr: str) -> List[Tuple[str, str, str, str]]:
    pattern = r'(\w+)\s*=\s*intersection_cc\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)'
    
    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        _, var1, var2, var3, var4 = match.groups()
        results.append((var1, var2, var3, var4))

    return results


def draw_intersection_cc(
    intersection_cc_info_list: List[Tuple[str, str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any
):
    for intersection_cc_info in intersection_cc_info_list:
        a, b, c, d = intersection_cc_info
        point_a = points_dict.get(a)
        point_b = points_dict.get(b)
        point_c = points_dict.get(c)
        point_d = points_dict.get(d)

        plot_dash_line(point_b, point_a, ax)
        plot_dash_line(point_b, point_d, ax)
        plot_dash_line(point_c, point_a, ax)
        plot_dash_line(point_c, point_d, ax)


def find_mirror_patterns(cstr: str) -> List[Tuple[str, str, str]]:
    pattern = r'(\w+)\s*=\s*mirror\s+(\w+)\s+(\w+)\s+(\w+)'
    
    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        _, var1, var2, var3 = match.groups()
        results.append((var1, var2, var3))

    return results


def draw_mirror(
    mirror_info_list: List[Tuple[str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any
):
    for mirror_info in mirror_info_list:
        a, b, c = mirror_info
        point_a = points_dict.get(a)
        point_b = points_dict.get(b)
        point_c = points_dict.get(c)

        plot_dash_line(point_a, point_c, ax)
        plot_dash_line(point_b, point_c, ax)


def find_midpoint_patterns(cstr: str) -> List[Tuple[str, str, str]]:
    pattern = r'(\w+)\s*=\s*midpoint\s+(\w+)\s+(\w+)\s+(\w+)'
    
    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        _, var1, var2, var3 = match.groups()
        results.append((var1, var2, var3))

    return results


def draw_midpoint(
    midpoint_info_list: List[Tuple[str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any
):
    for midpoint_info in midpoint_info_list:
        a, b, c = midpoint_info
        point_a = points_dict.get(a)
        point_b = points_dict.get(b)
        point_c = points_dict.get(c)

        plot_solid_line(point_b, point_c, ax)


def find_reflect_patterns(cstr: str) -> List[Tuple[str, str, str, str]]:
    pattern = r'(\w+)\s*=\s*reflect\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)'
    
    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        _, var1, var2, var3, var4 = match.groups()
        results.append((var1, var2, var3, var4))

    return results


def draw_reflect(
    reflect_info_list: List[Tuple[str, str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any
):
    for reflect_info in reflect_info_list:
        a, b, c, d = reflect_info
        point_a = points_dict.get(a)
        point_b = points_dict.get(b)
        point_c = points_dict.get(c)
        point_d = points_dict.get(d)

        plot_dash_line(point_a, point_c, ax)
        plot_dash_line(point_a, point_d, ax)
        plot_dash_line(point_b, point_c, ax)
        plot_dash_line(point_b, point_d, ax)
        plot_dash_line(point_a, point_b, ax)


def find_trisegment_patterns(cstr: str) -> List[Tuple[str, str, str, str, str]]:
    pattern = r'(\w+)\s+(\w+)\s*=\s*trisegment\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)'
    
    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        _, _, var1, var2, var3, var4 = match.groups()
        results.append((var1, var2, var3, var4))

    return results


def draw_trisegment(
    trisegment_info_list: List[Tuple[str, str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any
):
    for trisegment_info in trisegment_info_list:
        a, b, c, d = trisegment_info
        point_a = points_dict.get(a)
        point_b = points_dict.get(b)
        point_c = points_dict.get(c)
        point_d = points_dict.get(d)

        plot_solid_line(point_c, point_a, ax)
        plot_solid_line(point_a, point_b, ax)
        plot_solid_line(point_b, point_d, ax)


def find_intersection_lc_patterns(cstr: str) -> List[Tuple[str, str, str, str]]:
    pattern = r'(\w+)\s*=\s*intersection_lc\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)'
    
    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        _, var1, var2, var3, var4 = match.groups()
        results.append((var1, var2, var3, var4))

    return results


def draw_intersection_lc(
    intersection_lc_info_list: List[Tuple[str, str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any
):
    fill_missing(args, {"color": "blue", "lw": 1.5, "alpha": 0.9})

    for intersection_lc_info in intersection_lc_info_list:
        a, b, c, d = intersection_lc_info
        point_a = points_dict.get(a)
        point_b = points_dict.get(b)
        point_c = points_dict.get(c)
        point_d = points_dict.get(d)

        radius = np.sqrt(
            (point_a.num.x - point_c.num.x)**2 + 
            (point_a.num.y - point_c.num.y)**2
        )

        circle = plt.Circle(
            (point_c.num.x, point_c.num.y),
            radius,
            fill=False,
            **args
        )

        ax.add_patch(circle)

        plot_dash_line(point_c, point_a, ax)
        plot_dash_line(point_c, point_d, ax)


def find_on_line_patterns(cstr: str) -> List[Tuple[str, str, str]]:
    pattern = r'(\w+)\s*=\s*on_line\s+(\w+)\s+(\w+)\s+(\w+)'
    
    results = []
    matches = re.finditer(pattern, cstr)
    for match in matches:
        _, var1, var2, var3 = match.groups()
        results.append((var1, var2, var3))

    return results


def draw_on_line(
    on_line_info_list: List[Tuple[str, str, str]],
    points_dict: Dict[str, Point],
    ax: "Axes",
    **args: Any
):
    for on_line_info in on_line_info_list:
        a, b, c = on_line_info
        point_a = points_dict.get(a)
        point_b = points_dict.get(b)
        point_c = points_dict.get(c)

        plot_solid_line(point_a, point_b, ax)
        plot_solid_line(point_a, point_c, ax)


class DrawingCompletor:
    def __init__(
        self, cstr: str, points_dict: Dict[str, Point], ax: Axes
    ) -> None:
        self.cstr = cstr
        self.points_dict = points_dict
        self.ax = ax

    def complete(self):
        lconst_info_list = find_lconst_pattern(self.cstr)
        if lconst_info_list:
            draw_lconst(lconst_info_list, self.points_dict, self.ax)

        shift_info_list = find_shift_patterns(self.cstr)
        if shift_info_list:
            draw_shift(shift_info_list, self.points_dict, self.ax)

        lc_tangent_info_list = find_lc_tangent_patterns(self.cstr)
        if lc_tangent_info_list:
            draw_lc_tangent(lc_tangent_info_list, self.points_dict, self.ax)

        intersection_ll_info_list = find_intersection_ll_patterns(self.cstr)
        if intersection_ll_info_list:
            draw_intersection_ll(
                intersection_ll_info_list, self.points_dict, self.ax
                )
            
        on_circle_info_list = find_on_circle_patterns(self.cstr)
        if on_circle_info_list:
            draw_on_circle(
                on_circle_info_list, self.points_dict, self.ax
            )

        ninepoints_info_list = find_ninepoints_patterns(self.cstr)
        if ninepoints_info_list:
            draw_ninepoints(ninepoints_info_list, self.points_dict, self.ax)

        tangent_info_list = find_tangent_patterns(self.cstr)
        if tangent_info_list:
            draw_tangent(tangent_info_list, self.points_dict, self.ax)

        circle_info_list = find_circle_patterns(self.cstr)
        if circle_info_list:
            draw_circumcenter(circle_info_list, self.points_dict, self.ax)

        circumcenter_info_list = find_circumcenter_patterns(self.cstr)
        if circumcenter_info_list:
            draw_circumcenter(circumcenter_info_list, self.points_dict, self.ax)

        triangle_info_list = find_triangle_patterns(self.cstr)
        if triangle_info_list:
            draw_triangle(triangle_info_list, self.points_dict, self.ax)

        iso_triangle_vertex_info_list = find_iso_triangle_vertex_patterns(self.cstr)
        if iso_triangle_vertex_info_list:
            draw_iso_triangle_vertex(
                iso_triangle_vertex_info_list, self.points_dict, self.ax
            )

        parallelogram_info_list = find_parallelogram_patterns(self.cstr)
        if parallelogram_info_list:
            draw_parallelogram(
                parallelogram_info_list, self.points_dict, self.ax
            )

        centroid_info_list = find_centroid_patterns(self.cstr)
        if centroid_info_list:
            draw_centroid(
                centroid_info_list, self.points_dict, self.ax
            )

        eqratio6_info_list = find_eqratio6_patterns(self.cstr)
        if eqratio6_info_list:
            draw_eqratio6(
                eqratio6_info_list, self.points_dict, self.ax
            )

        eqratio_info_list = find_eqratio_patterns(self.cstr)
        if eqratio_info_list:
            draw_eqratio(
                eqratio_info_list, self.points_dict, self.ax
            )

        eqdistance_info_list = find_eqdistance_patterns(self.cstr)
        if eqdistance_info_list:
            draw_eqdistance(
                eqdistance_info_list, self.points_dict, self.ax
            )

        intersection_cc_info_list = find_intersection_cc_patterns(self.cstr)
        if intersection_cc_info_list:
            draw_intersection_cc(
                intersection_cc_info_list, self.points_dict, self.ax
            )

        mirror_info_list = find_mirror_patterns(self.cstr)
        if mirror_info_list:
            draw_mirror(
                mirror_info_list, self.points_dict, self.ax
            )

        midpoint_info_list = find_midpoint_patterns(self.cstr)
        if midpoint_info_list:
            draw_midpoint(
                midpoint_info_list, self.points_dict, self.ax
            )

        reflect_info_list = find_reflect_patterns(self.cstr)
        if reflect_info_list:
            draw_reflect(
                reflect_info_list, self.points_dict, self.ax
            )

        trisegment_info_list = find_trisegment_patterns(self.cstr)
        if trisegment_info_list := find_trisegment_patterns(self.cstr):
            draw_trisegment(
                trisegment_info_list, self.points_dict, self.ax
            )

        intersection_lc_info_list = find_intersection_lc_patterns(self.cstr)
        if intersection_lc_info_list:
            draw_intersection_lc(
                intersection_lc_info_list, self.points_dict, self.ax
            )

        on_line_info_list = find_on_line_patterns(self.cstr)
        if on_line_info_list:
            draw_on_line(
                on_line_info_list, self.points_dict, self.ax
            )