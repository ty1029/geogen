base_scenes = [
    {
        "before": 'a = free a; b = segment b a; c = nsquare c a b; d = angle_bisector d a b c, on_line d a c; e = foot e c b d ? rconst b d c e 2',
        'after': 'a = free a; b = segment b a; c = nsquare c a b; d = angle_bisector d a b c, on_line d a c; e = foot e c b d; f = intersection_ll f b a c e ? rconst b d c e 2',
        "note": "",
        "page": "13, 第九题"
    },
    {
        "before": 'd = free d; c = segment c d; o = on_bline o d c; a = foot a d o c; b = foot b c o d ? rconst a d b c 1',
        "after": "d = free d; c = segment c d; o = on_bline o d c; a = foot a d o c; b = foot b c o d; e = intersection_ll e d a c b ? rconst a d b c 1",
        "note": "不加辅助线也可以直接获得答案",
        "page": "12, 第七题"
    },
    {
        "before": "b = free b; d = segment d b; c = midpoint c b d; a = segment a c; f = midpoint f a c; e = intersection_ll e a b d f ? rconst e f f d 1/3",
        "after": "b = free b; d = segment d b; c = midpoint c b d; a = segment a c; f = midpoint f a c; e = intersection_ll e a b d f; g = on_pline g c d e, on_line g a b ? rconst e f f d 1/3",
        "note": "加了辅助线也无法获得答案",
        "page": "16, 例2"
    },
    {
        'before': "a b c = triangle a b c; m = on_line m a c, angle_bisector m a b c; n = on_line n a b, angle_bisector n a c b; p = intersection_ll p c n b m ? eqangle a b a p a p a c",
        "after": "a b c = triangle a b c; m = on_line m a c, angle_bisector m a b c; n = on_line n a b, angle_bisector n a c b; p = intersection_ll p c n b m; d = foot d p a b; f = foot f p a c ? eqangle a b a p a p a c",
        "note": "不加辅助线也可以获得答案",
        "page": "21, 例3"
    },
    {
        'before': "a = free a; b = segment b a; c = nsquare c a b; d = angle_bisector d a b c, on_line d a c; e = foot e c b d ? rconst b d c e 2",
        "after": "a = free a; b = segment b a; c = nsquare c a b; d = angle_bisector d a b c, on_line d a c; e = foot e c b d; f = intersection_ll f c e b a ? rconst b d c e 2",
        "note": "",
        "page": "22, 例2"
    },
    {
        "note": "过于复杂无法编译",
        "page": "22, 例3"
    },
    {
        "before": "a d c b = eq_quadrangle a d c b; e = midpoint e b c; f = midpoint f a d; g = intersection_ll g b a e f; h = intersection_ll h c d e f ? eqangle g b g e h c h e",
        "after": "a d c b = eq_quadrangle a d c b; e = midpoint e b c; f = midpoint f a d; g = intersection_ll g b a e f; h = intersection_ll h c d e f; m = midpoint m b d ? eqangle g b g e h c h e",
        "note": "如果只有 caption 是可以编译成功的，但是加上问题就编译不成功了",
        "page": "31, 例2"
    },
    {
        "before": "a = free a; b = segment b a; c = nsquare c a b; d = angle_bisector d c b a, on_line d a c; e = foot e c b d ? rconst b d c e 2",
        "after": "a = free a; b = segment b a; c = nsquare c a b; d = angle_bisector d c b a, on_line d a c; e = foot e c b d; f = intersection_ll f b a c e ? rconst b d c e 2",
        "note": "",
        "page": "32, 例6"
    },
    {
        "before": "b c d a = r_trapezoid b c d a; e = foot e b d c ? rconst a d d e 1",
        "after": "",
        "note": "辅助线无法添加，本身就存在，而且梯形总是短边的位置不对(这个是最奇葩的，无法怎么换点的顺序，始终是AD是长边)，如果修改题目，从a向dc做垂线，那直接就编译不通过了",
        "page": "48, 例9"
    }
]

{
    "base_scene":"a b c = triangle a b c; d = angle_bisector d b a c, on_line d b c; e = foot e b a d; f = on_pline0 f e a c, on_line f a b ? rconst a f b f 1",
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
    "base_scene":"a b c = risos a b c; p = on_line p b c; e = foot e p a b; f = foot f p a c ? risos d e f",
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
    "base_scene":"a b c = triangle a b c; e = foot e b a c; f = foot f c a b; m = midpoint m e f ? r_triangle d m e",
    "aux_clause":""
}



{
    "base_scene":"a b c = triangle a b c; i = incenter i a b c; d = foot d i b c; e = foot e i a c; f = foot f i a b; p = on_pline0 p f a c, rconst f p f b 1; q = on_pline0 q e a c, rconst e q e c 1 ? coll p q d",
    "aux_clause":"",
    "source":"2018 Iran MO 3rd-G1",
    "note":"缺少内切圆切点直接定义，这里用内心的垂足定义"
},
{
    "base_scene":"a b c = triangle a b c, rconst a b a c 1; m = midpoint m b c; p = on_pline0 p a b c; x = on_line x p b; y = on_line y p c, eqangle x p x m y p y m ? cyclic a p x y",
    "aux_clause":"q = intersection_ll q p a x y; s = intersection_ll s x m p c; t = intersection_ll t y m a b",
    "source":"2019 Hong Kong TST D3-P2"
},
{
    "base_scene":"a b c = triangle a b c; o = circumcenter o a b c; d = cyclic d a b c, rconst d a d b 1; e = intersection_ll a d b c; z = on_line z a b, cyclic b d e z; h = on_line h a c, cyclic a d z h ? rconst b e a h 1",
    "aux_clause":"",
    "source":"2019 Greece MO-P2",
    "note":"线圆交点定义太特殊，一般情况无法定义"
},
{
    "base_scene":"a b c = triangle a b c; d = foot d a b c; e = foot e b a c; f = foot f c a b; a1 = foot a1 f b c; b1 = foot b1 d a c; c1 = foot c1 e a b ? simtri a b c a1 b1 c1",
    "aux_clause":"a2 = foot a2 e b c; b2 = foot b2 f a c; c2 = foot c2 d a b",
    "source":"2016 Iran MO 3rd-G3"
},
{
    "base_scene":"a b c = triangle a b c; d = angle_bisector d b a c, on_line d b c; e = angle_bisector e a b c, on_line e a c; f = angle_bisector f a c b, on_line f a b; m = on_line m e f; n = on_line n e f, rconst a m a n 1; h = foot h a b c; k = on_line k e f; l = on_line l e f, simtri a k l h m n ? rconst d k d l 1",
    "aux_clause":"w = intersection_ll e f b c; v = foot v a e f; u = foot u d e f; p = on_line p d u, simtri u a p u d a; q = intersection_ll a p e f; r = intersection_ll a h e f",
    "source":"2016 Iran MO 3rd-G6"
}