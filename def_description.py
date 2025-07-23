DEF_DESCRIPTION = {
    "angle_bisector": {
        "input": ['x', 'a', 'b', 'c'],
        "description": "From non-collinear points {a}, {b}, {c}, creates {x} in the internal bisector of angle {a}{b}{c}, with vertex at {b}."
    },
    "angle_mirror": {
        "input": ['x', 'a', 'b', 'c'],
        "description": "From non-collinear points {a}, {b}, {c}, creates {x} on the opposite side of {b}{c} with respect to {a} in a way that angle {a}{b}{x} doubles angle {a}{b}{c}."
    },
    "circle": {
        "input": ['x', 'a', 'b', 'c'],
        "description": "From non-collinear points {a}, {b}, {c}, creates {x} the center of the circle through {a}, {b}, {c}."
    },
    "circumcenter": {
        "input": ['x', 'a', 'b', 'c'],
        "description": "From non-collinear points {a}, {b}, {c}, creates {x} the center of the circle through {a}, {b}, {c}."
    },
    "eq_quadrangle": {
        "input": ['a', 'b', 'c', 'd'],
        "description": "From nothing, adds four points in a quadrilateral {a}{b}{c}{d} with two opposing sides ({a}{d} and {b}{c}) of same length."
    },
    "iso_trapezoid": {
        "input": ['a', 'b', 'c', 'd'],
        "description": "From nothing, adds four points on a trapezoid {a}{b}{c}{d} with parallel opposing sides {a}{b} and {c}{d} and non-parallel opposing sides {a}{d} and {b}{c} of same length. Adds the congruence statement that {a}{d}={b}{c} and the parallel statement that {a}{b}//{c}{d}."
    },
    "eq_triangle": {
        "input": ['x', 'b', 'c'],
        "description": "From two different points {b}, {c}, adds a third point {x} such that the triangle {x}{b}{c} is equilateral."
    },
    "eqangle2": {
        "input": ['x', 'a', 'b', 'c'],
        "description": "From three non-collinear points {a}, {b}, {c}, adds a point {x} such that the quadrilateral {a}{b}{c}{x} has two opposite angles that are congruent, ∠{b}{a}{x} and ∠{b}{c}{x}."
    },
    "eqdia_quadrangle": {
        "input": ['a', 'b', 'c', 'd'],
        "description": "From nothing, adds four points on a quadrilateral {a}{b}{c}{d} with the two diagonals of same length."
    },
    "eqdistance": {
        "input": ['x', 'a', 'b', 'c'],
        "description": "From two different points {b}, {c}, and with a base point {a} (that can be either {b} or {c} itself), adds {x} such that the distance from {x} to {a} is equal to the distance from {b} to {c}."
    },
    "foot": {
        "input": ['x', 'a', 'b', 'c'],
        "description": "From three non-collinear points {a}, {b}, {c}, adds {x} that is the perpendicular projection of {a} onto line {b}{c}."
    },
    "free": {
        "input": ['a'],
        "description": "From nothing, adds point {a} with random coordinates."
    },
    "incenter": {
        "input": ['x', 'a', 'b', 'c'],
        "description": "From three non-collinear points {a}, {b}, {c}, adds {x} the incenter of the triangle {a}{b}{c}. It acknowledges the fact that it is the intersection of the three internal bisectors of the angles of the triangle."
    },
    "incenter2": {
        "input": ['x', 'y', 'z', 'i', 'a', 'b', 'c'],
        "description": "From three non-collinear points {a}, {b}, {c}, adds {i}, the incenter of the triangle {a}{b}{c}, as well as {x}, {y}, and {z}, the tangent points of the incircle with sides {b}{c}, {a}{c}, and {a}{b}, respectively."
    },
    "excenter": {
        "input": ['x', 'a', 'b', 'c'],
        "description": "From three non-collinear points {a}, {b}, {c}, adds {x} the excenter of triangle {a}{b}{c} in a way that the corresponding excircle is externally tangent to side {b}{c}."
    },
    "excenter2": {
        "input": ['x', 'y', 'z', 'i', 'a', 'b', 'c'],
        "description": "From three non-collinear points {a}, {b}, {c}, adds {i}, the excenter of the triangle {a}{b}{c} in a way that the corresponding excircle is externally tangent to side {b}{c}. It also adds {x}, {y}, and {z}, the tangent points of the excircle with the lines containing sides {b}{c}, {a}{c}, and {a}{b}, respectively."
    },
    "centroid": {
        "input": ['x', 'y', 'z', 'i', 'a', 'b', 'c'],
        "description": "From three non-collinear points {a}, {b}, {c}, adds {i}, the centroid of the triangle. It also adds {x}, {y}, and {z}, the midpoints of sides {b}{c}, {a}{c}, and {a}{b}, respectively."
    },
    "ninepoints": {
        "input": ['x', 'y', 'z', 'i', 'a', 'b', 'c'],
        "description": "From three non-collinear points {a}, {b}, {c}, adds {x}, {y}, and {z}, the midpoints of sides {b}{c}, {a}{c}, and {a}{b}, respectively. It also adds {i}, the center of the circle going through {x}, {y}, and {z}, which is also the nine points circle of the triangle {a}{b}{c}."
    },
    "intersection_cc": {
        "input": ['x', 'o', 'w', 'a'],
        "description": "From three non-collinear points {o}, {w}, and {a}, adds {x}, the other intersection of the circle of center {o} through {a} and the circle of center {w} through {a}."
    },
    "intersection_lc": {
        "input": ['x', 'a', 'o', 'b'],
        "description": "From three points, {a}, {o}, and {b}, {b} different from both {a} and {o}, such that {b}{o} is not perpendicular to {b}{a} (to avoid the situation of a line tangent to a circle at {b}), adds point {x}, the second intersection of line {a}{b} with the circle of center {o} going through {b}."
    },
    "intersection_ll": {
        "input": ['x', 'a', 'b', 'c', 'd'],
        "description": "From four points {a}, {b}, {c}, {d}, such that lines {a}{b} and {c}{d} are not parallel and such that they do are not all collinear, build point {x} on the intersection of lines {a}{b} and {c}{d}."
    },
    "intersection_lp": {
        "input": ['x', 'a', 'b', 'c', 'm', 'n'],
        "description": "From five points {a}, {b}, {c}, {m}, and {n}, such that lines {a}{b} and {m}{n} are not parallel, and that {c} is neither on line {a}{b} nor on line {m}{n}, builds {x}, the intersection of line {a}{b} with the line through {c} that is parallel to {m}{n}."
    },
    "intersection_lt": {
        "input": ['x', 'a', 'b', 'c', 'd', 'e'],
        "description": "From five points {a}, {b}, {c}, {d}, and {e}, such that lines {a}{b} and {d}{e} are not perpendicular and {c} is not on line {a}{b}, build {x}, the intersection of line {a}{b} and the line through {c} perpendicular to {d}{e}."
    },
    "intersection_pp": {
        "input": ['x', 'a', 'b', 'c', 'd', 'e', 'f'],
        "description": "From six points, {a}, {b}, {c}, {d}, {e}, {f}, such that {a} and {d} are different and that lines {b}{c} and {e}{f} are not parallel, builds point {x} in the intersection of the line through {a} parallel to {b}{c} and the line through {d} parallel to {e}{f}."
    },
    "intersection_tt": {
        "input": ['x', 'a', 'b', 'c', 'd', 'e', 'f'],
        "description": "From six points, {a}, {b}, {c}, {d}, {e}, {f}, such that {a} and {d} are different and lines {b}{c} and {e}{f} are not parallel, build point {x} in the intersection of the line through {a} perpendicular to {b}{c} and the line through {d} perpendicular to {e}{f}."
    },
    "iso_triangle": {
        "input": ['a', 'b', 'c'],
        "description": "From nothing, creates the three vertices {a}, {b}, {c} of an isosceles triangle with {a}{b}={a}{c}."
    },
    "lc_tangent": {
        "input": ['x', 'a', 'o'],
        "description": "From two different points {a}, {o}, builds {x}, a point on the line perpendicular to {a}{o} through {a} (the line tangent to the circle of center {o} through {a}, with tangent point {a})."
    },
    "midpoint": {
        "input": ['x', 'a', 'b'],
        "description": "From a pair of points {a}, {b}, that are different, builds {x}, the midpoint of {a} and {b}."
    },
    "mirror": {
        "input": ['x', 'a', 'b'],
        "description": "From two points {a}, {b} that are different, builds {x}, the reflection of point {a} with respect to point {b} (so that {b} is the midpoint of {a}{x})."
    },
    "nsquare": {
        "input": ['x', 'a', 'b'],
        "description": "Given two distinct points {a}, {b}, builds {x} such that the triangle {x}{a}{b} is an isosceles right triangle."
    },
    "on_aline": {
        "input": ['x', 'a', 'b', 'c', 'd', 'e'],
        "description": "From five points {a}, {b}, {c}, {d}, {e}, such that {c}, {d}, {e} are non-collinear, adds point {x} in a way that the angle {b}{a}{x} is the same as the angle {e}{d}{c} (up to a rotation and a translation)."
    },
    "on_bline": {
        "input": ['x', 'a', 'b'],
        "description": "Given two distinct points {a}, {b}, builds {x}, a point on the perpendicular bisector of the segment {a}{b}."
    },
    "on_circle": {
        "input": ['x', 'o', 'a'],
        "description": "From two distinct points {o}, {a}, builds {x}, a point on the circle of center {o} through {a}."
    },
    "on_line": {
        "input": ['x', 'a', 'b'],
        "description": "From two distinct points {a}, {b}, builds {x}, another point on the line {a}{b}."
    },
    "on_pline": {
        "input": ['x', 'a', 'b', 'c'],
        "description": "From three non-collinear points {a}, {b}, {c}, with {b} different from {c}, builds {x} on the line parallel to {b}{c} through {a}."
    },
    "on_tline": {
        "input": ['x', 'a', 'b', 'c'],
        "description": "From three points {a}, {b}, {c}, with {b} different from {c}, builds {x} on the line through {a} perpendicular to {b}{c}."
    },
    "orthocenter": {
        "input": ['x', 'a', 'b', 'c'],
        "description": "From three non-collinear points {a}, {b}, {c}, builds {x}, the orthocenter of the triangle {a}{b}{c}."
    },
    "parallelogram": {
        "input": ['a', 'b', 'c', 'x'],
        "description": "From three non-collinear points {a}, {b}, {c}, builds {x} such that {a}{b}{c}{x} is a parallelogram."
    },
    "pentagon": {
        "input": ['a', 'b', 'c', 'd', 'e'],
        "description": "From nothing, creates five points {a}, {b}, {c}, {d}, {e}. The coordinates are a random conformal deformation (isometry combined with scaling) of a random inscribed convex pentagon."
    },
    "psquare": {
        "input": ['x', 'a', 'b'],
        "description": "From two points {a}, {b} that are distinct, builds {x} the image of {b} under a rotation of 90 degrees around {a}."
    },
    "quadrangle": {
        "input": ['a', 'b', 'c', 'd'],
        "description": "From nothing, creates four points, {a}, {b}, {c}, {d} which are vertices of a random convex quadrilateral."
    },
    "r_trapezoid": {
        "input": ['a', 'b', 'c', 'd'],
        "description": "From nothing, creates {a}, {b}, {c}, {d}, the four vertices of a trapezoid with parallel sides {a}{b} and {c}{d}, and a right angle at {a}."
    },
    "r_triangle": {
        "input": ['a', 'b', 'c'],
        "description": "From nothing, creates {a}, {b}, {c} the vertices of a right triangle with a right angle at {a}."
    },
    "rectangle": {
        "input": ['a', 'b', 'c', 'd'],
        "description": "From nothing, creates {a}, {b}, {c}, {d} the four vertices of rectangle {a}{b}{c}{d}."
    },
    "reflect": {
        "input": ['x', 'a', 'b', 'c'],
        "description": "From three non-collinear points {a}, {b}, {c}, in particular with {b} different from {c}, builds {x} the reflection of {a} by the line {b}{c}."
    },
    "risos": {
        "input": ['a', 'b', 'c'],
        "description": "From nothing, builds {a}, {b}, {c} such that the triangle {a}{b}{c} is an isosceles right triangle with a right angle at {a}."
    },
    "segment": {
        "input": ['a', 'b'],
        "description": "From nothing, adds two points {a}, {b}, with random coordinates."
    },
    "shift": {
        "input": ['x', 'b', 'c', 'd'],
        "description": "From three points {b}, {c}, {d}, with {b} different from {d}, build {x}, the translation of {b} by the vector from {d} to {c}."
    },
    "square": {
        "input": ['a', 'b', 'x', 'y'],
        "description": "From two points {a}, {b}, with {a} different from {b}, builds {x}, {y}, the other two vertices of a square with side {a}{b}."
    },
    "isquare": {
        "input": ['a', 'b', 'c', 'd'],
        "description": "From nothing, creates the four vertices of a square {a}{b}{c}{d}."
    },
    "trapezoid": {
        "input": ['a', 'b', 'c', 'd'],
        "description": "From nothing, creates four vertices of a trapezoid {a}{b}{c}{d}, with {a}{b} parallel to {c}{d}."
    },
    "triangle": {
        "input": ['a', 'b', 'c'],
        "description": "From nothing, creates three points {a}, {b}, and {c}, with random coordinates."
    },
    "triangle12": {
        "input": ['a', 'b', 'c'],
        "description": "From nothing, builds the three vertices {a}, {b}, {c} of a triangle such that the proportion {a}{b}:{a}{c} is 1:2."
    },
    "2l1c": {
        "input": ['x', 'y', 'z', 'i', 'a', 'b', 'c', 'o'],
        "description": "Given three points {o}, {a}, {b}, with {b} in the center through {a} of center {o}, and {c} a point not in the line {a}{b}, builds {i}, the center of a circle tangent to the circle centered at {o} through {a}, to the line {a}{c} and to the line {b}{c}. It also builds the tangency points {x} to {a}{c}, {y} to {b}{c} and {z} to the circle of center {o} through {a}."
    },
    "e5128": {
        "input": ['x', 'y', 'a', 'b', 'c', 'd'],
        "description": "Given four points {a}, {b}, {c}, {d}, with {b}{c}={c}{d} and {b}{c} perpendicular to {b}{a}, builds {y} the midpoint of {a}{b} and {x} the intersection of line {d}{y} and the circle centered at {c} through {b}. It transfers the angle {b}{a}{d} to {a}{x}{y} in a specific way."
    },
    "3peq": {
        "input": ['x', 'y', 'z', 'a', 'b', 'c'],
        "description": "Given three non-collinear points {a}, {b}, {c}, builds points {x} on the extended side {a}{b}, {y} in the extended side {a}{c}, and {z} on the extended side {b}{c} of triangle {a}{b}{c} in a way that {z} is the midpoint of {x}{y}."
    },
    "trisect": {
        "input": ['x', 'y', 'a', 'b', 'c'],
        "description": "From three non-collinear points {a}, {b}, {c}, builds {x}, {y}, the points on segment {a}{c} that trisect the angle {a}{b}{c}."
    },
    "trisegment": {
        "input": ['x', 'y', 'a', 'b'],
        "description": "Given two different points {a}, {b}, builds {x}, {y} the two points trisecting the segment {a}{b}."
    },
    "on_dia": {
        "input": ['x', 'a', 'b'],
        "description": "Given two different points {a}, {b}, builds {x} a point such that the triangle {a}{x}{b} is a right triangle with a right angle at {x}."
    },
    "ieq_triangle": {
        "input": ['a', 'b', 'c'],
        "description": "From nothing, creates the three vertices of an equilateral triangle {a}{b}{c}."
    },
    "cc_tangent": {
        "input": ['x', 'y', 'z', 'i', 'o', 'a', 'w', 'b'],
        "description": "From four points {o}, {a}, {w}, {b}, such that {o} is neither {a} nor {w}, and such that {w} and {b} are distinct, builds {x}, {y}, {z}, {i} on a pair of lines {x}{y} and {z}{i} that are simultaneously tangent to both the circle of center {o} through {a} and the circle of center {w} through {b}. {x} and {z} are the tangent points on the circle centered at {o} through {a}, and {y} and {i} are the tangent points on the circle centered at {w} through {b}."
    },
    "eqangle3": {
        "input": ['x', 'a', 'b', 'd', 'e', 'f'],
        "description": "From five points {a}, {b}, {d}, {e}, {f} disposed in a way that {a} is distinct from {b} and {d}, {e}, {f} form a non-degenerate triangle, builds {x} the vertex of an angle in such a way that the angles {a}{x}{b} and {e}{d}{f} are the same (up to a rotation and a translation)."
    },
    "tangent": {
        "input": ['x', 'y', 'a', 'o', 'b'],
        "description": "From three different points {a}, {b}, {o}, builds {x} and {y}, the points of tangency of the two lines through {a} tangent to the circle of center {o} through {b}."
    },
    "on_circum": {
        "input": ['x', 'a', 'b', 'c'],
        "description": "From three non-collinear points {a}, {b}, and {c}, builds {x} a point on the circle through {a}, {b}, and {c}."
    },
    "on_pline0": {
        "input": ['x', 'a', 'b', 'c'],
        "description": "From three points {a}, {b}, {c}, with {b} different from {c}, builds {x} on the line parallel to {b}{c} through {a}."
    },
    "iso_triangle0": {
        "input": ['a', 'b', 'c'],
        "description": "From nothing, creates the three vertices {a}, {b}, {c} of an isosceles triangle with {a}{b} = {a}{c}."
    },
    "iso_triangle_vertex": {
        "input": ['x', 'b', 'c'],
        "description": "From two points {b}, {c} that are distinct, builds {x}, the vertex of an isosceles triangle with base {b}{c}."
    },
    "iso_triangle_vertex_angle": {
        "input": ['x', 'b', 'c'],
        "description": "From two points {b}, {c} that are distinct, builds {x}, the vertex of an isosceles triangle with base {b}{c}, and ensures the equality of base angles."
    },
    "on_aline0": {
        "input": ['x', 'a', 'b', 'c', 'd', 'e', 'f', 'g'],
        "description": "From seven points {a}, {b}, {c}, {d}, {e}, {f}, {g}, with the constraint that {a}, {b}, {c}, and {d} do not lie all on the same line, builds {x} such that the angle formed at the intersection of lines {e}{f} and {g}{x} is the same (up to a rotation and a translation) as the angle formed at the intersection between lines {a}{b} and {c}{d}."
    },
    "eqratio": {
        "input": ['x', 'a', 'b', 'c', 'd', 'e', 'f', 'g'],
        "description": "From seven points {a}, {b}, {c}, {d}, {e}, {f}, {g}, builds {x}, a point such that {a}{b}/{c}{d} = {e}{f}/{g}{x}."
    },
    "eqratio6": {
        "input": ['x', 'a', 'c', 'e', 'f', 'g', 'h'],
        "description": "From six points {a}, {c}, {e}, {f}, {g}, {h}, builds {x}, a point such that {a}{x}/{c}{x} = {e}{f}/{g}{h}."
    },
    "rconst": {
        "input": ['a', 'b', 'c', 'x', 'r'],
        "description": "Given three points {a}, {b}, {c} such that {a} is different from {b}, and a fraction {r}, builds {x}, a point such that {a}{b}/{c}{x} = {r}."
    },
    "rconst2": {
        "input": ['x', 'a', 'b', 'r'],
        "description": "Given two points {a}, {b} that are distinct, and a fraction {r}, builds {x}, a point such that {a}{x}/{b}{x} = {r}."
    },
    "aconst": {
        "input": ['a', 'b', 'c', 'x', 'r'],
        "description": "Given three points {a}, {b}, {c}, with {a}, {b} distinct, and an angle {r}, builds {x}, a point such that the angle from line {a}{b} to line {c}{x} taken counterclockwise is {r}."
    },
    "s_angle": {
        "input": ['a', 'b', 'x', 'y'],
        "description": "Given two points {a}, {b} that are distinct, and an angle {y}, builds {x}, a point such that the angle from line {a}{b} to line {b}{x} taken counterclockwise is {y}."
    },
    "lconst": {
        "input": ['x', 'a', 'l'],
        "description": "From a point {a}, builds {x} with an integer distance {l} from {a} to {x}."
    },
    "eqangle": {
        "input": ['b', 'a', 'b', 'c', 'y', 'x', 'y', 'z'],
        "description": "Angle {a}{b}{c} equals angle {x}{y}{z}"
    },
    "PythagoreanPremises": {
        "input": ['a', 'b', 'c'],
        "description": "{a}{b}{c} is in the form of a right angled triangle. {a}{b} is perpendicular to {a}{c}"
    },
    "PythagoreanConclusions": {
        "input": ['a', 'b', 'c'],
        "description": "{a}{b}{c} is in the form of a right angled triangle. {a}{b} is perpendicular to {a}{c}"
    },
    "simtrir": {
        "input": ['a', 'b', 'c', 'p', 'q', 'r'],
        "description": "Triangles {a}{b}{c} and {p}{q}{r} are similar under orientation-preserving transformations taking {a} to {p}, {b} to {q} and {c} to {r}."
    },
    "simtri": {
        "input": ['a', 'b', 'c', 'p', 'q', 'r'],
        "description": "Triangles {a}{b}{c} and {p}{q}{r} are similar under orientation-preserving transformations taking {a} to {p}, {b} to {q} and {c} to {r}."
    },
    "para": {
        "input": ['a', 'b', 'c', 'd'],
        "description": "Line {a}{b} and line {c}{d} are parallel."
    },
    "cyclic": {
        "input": ['x', 'a', 'b', 'c'],
        "description": "{x} is a point on the circle through {a}, {b}, and {c}."
    },
    "perp": {
        "input": ['a', 'b', 'c', 'd'],
        "description": "Line {a}{b} is perpendicular to line {c}{d}."
    },
    "coll": {
        "input": ['a', 'b', 'c'],
        "description": "Points {a}, {b}, and {c} are collinear."
    },
    "midp": {
        "input": ['x', 'a', 'b'],
        "description": "Points {x} is the midpoint of line {a}{b}"
    },
    "cong": {
        "input": ['a', 'b', 'c', 'd'],
        "description": "Line {a}{b} is equal to line {c}{d}."
    },
    "eqratio3": {
        "input": ['a', 'b', 'c', 'd', 'm', 'n'],
        "description": "Represent three eqratios through a list of 6 points (due to parallel lines). It can be viewed as in an instance of Thales theorem which has {a}{b} // {m}{n} // {c}{d}. It thus represent the corresponding eqratios: {m}{a} / {m}{c} = {n}{b} / {n}{d} and {a}{m} / {a}{c} = {b}{n} / {b}{d} and {m}{c} / {a}{c} = {n}{d} / {b}{d}"
    },
}