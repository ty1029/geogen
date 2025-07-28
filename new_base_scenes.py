base_scenes = [
    {
        "base_scene":"a b c = triangle a b c; d = angle_bisector d b a c, on_line d b c; e = foot b a d; f = on_pline0 f e a c, on_line f a b ? rconst a f b f 1",
        "aux_clause":"g = intersection_ll g b e a c"
    },
    {
        "base_scene":"a b c d = trapezoid a b c d; c a b = r_triangle c a b; d a b =r_triangle d a b ? rconst a c b d 1",
        "aux_clause":"o = midpoint o a b"
    },
    {
        "base_scene":"b c d a = trapezoid b c d a; e = midpoint e b d; f = midpoint f a c ? trapezoid a d f e",
        "aux_clause":"g = intersection_ll g d f b c"
    },
    {
        "base_scene":"a b c d = rectangle a b c d; e = on_line e b c, rconst a c c e 1; f = midpoint f a e ? r_triangle f b d",
        "aux_clause":""
    },
    {
        "base_scene":"a b c = triangle a b c; d = midpoint d b c; e = on_line e a d; f = on_bline f a e, on_line f b e ? rconst a c b e 1",
        "aux_clause":"g = on_line g a d, rconst a d d g 1; f = on_line f e d, rconst e d d f 1"
    },
    {
        "base_scene":"a b c = triangle a b c; d = on_line d b c, angle_bisector d b a c; e = midpoint e b c; g = on_pline g e a d, on_line g a b; f = intersection_ll f e g c a ? rconst b g c f 1",
        "aux_clause":"h = on_line h e f, rconst e f e h 1"
    },
    {
        "base_scene":"a b c = risos a b c; p = on_line p b c; e = foot p a b; f = foot p a c ? risos d e f",
        "aux_clause":""
    },
    {
        "base_scene":"a b c = risos a b c; d = midpoint d b c; e = on_line e b a; f = lc_tangent f d e, on_line f a c ? rconst d e d f 1",
        "aux_clause":""
    },
    {
        "base_scene":"a b c = triangle a b c; d = midpoint d b c; f = midpoint f a d ? rconst a c a e 3",
        "aux_clause":"g = on_line g a d, rconst a d d f 1; h = intersection_ll h b e g c"
    },
    {
        "base_scene":"a d c b = r_trapezoid a d c b; m = midpoint m d c ? rconst a m b m 1",
        "aux_clause":"e = intersection_ll a m b c"
    },
    {
        "base_scene":"a b c = iso_triangle a b c; o = midpoint o a b; d = on_dia d a b, on_line d a c; e = on_dia e b a, on_line e b c ? rconst d e b e 1",
        "aux_clause":""
    },
    {
        "base_scene":"a b c = r_triangle c a b; o = on_line o a c; d = on_circle d o a, on_line d a b; f = midpoint f d b; e = on_bline e d b, on_line e b c ? lc_tangent e d o",
        "aux_clause":""
    },
    {
        "base_scene":"a b c = triangle a b c; e = on_line e b c; d = on_line d b c, rconst e c e d 1; f = intersection_lp f a e d a b; rconst d f a c 1 ? eqangle a e a b a e a c",
        "aux_clause":"g = on_line g a e, rconst f e e g 1"
    },
    {
        "base_scene":"a b c = iso_triangle a b c; d = angle_bisector d a b c, on_line d a c; m = angle_bisector m b a c, on_line m b c; n = foot n d b c; g = lc_tangent g d b, on_line g a b; f = lc_tangent f d b, on_line f b c ? rconst b f m n 4",
        "aux_clause":"h = on_line h a b, on_pline0 h d b c"
    },
    {
        "base_scene":"a b c = triangle a b c; o = on_bline o a b, on_bline o a c; d = foot d a b c; m = angle_bisector m c a b, on_line m b c ? eqangle a o a m a m a d",
        "aux_clause":"e = on_line e a o, on_circle e o a"
    },
    {
        "base_scene":"a b c = triangle a b c; d = midpoint d b c; f = on_line f a d; e = on_line e b f, rconst a e e f 1 ? rconst b f a c 1",
        "aux_clause":"m = on_line m a d, rconst f d d m 1"
    },
    {
        "base_scene":"a b c d = quadrangle a b c d; e = midpoint e a d; f = midpoint f b c; g = midpoint g b d; h = midpoint h a c ? parallelogram e h f g",
        "aux_clause":""
    },
    {
        "base_scene":"a b c = risos a b c; d = midpoint d a c; e = foot e a b d; f = on_line f a e, on_line f b c ? rconst b f f c 2",
        "aux_clause":"n = foot n c b d"
    },
    {
        "base_scene":"a b c = triangle a b c; n = midpoint n b c; d = on_dia d a b; e = foot e c a d ? rconst n e n d 1",
        "aux_clause":"m = on_line m e n, on_line m b d"
    },
    {
        "base_scene":"a b c = triangle a b c; e = foot b a c; f = foot c a b; m = midpoint m e f ? r_triangle d m e",
        "aux_clause":""
    }
]