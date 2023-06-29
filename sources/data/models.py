# Language, lang_tag, slnt, EXTD, SPED, UC, lc

lang_dict = {
    "arg":
    {"language": "Argentina",
        "axes": {
            "slnt": 0,
            "EXTD": 452,
            "SPED": 0
        },
     "UC":
     "A.cur B.cur C.cur D.dec E.cur F.dec G.cur H.dec I.cur J.cur K.cur L.cur M.cur N.cur O.cur P.dec Q.cur R.dec S.cur T.dec U.cur V.cur W.cur X.dec Y.cur Z.cur",
     "lc":
     "a.mod b.lop c.mod d.mod e.ful f.mrr g.jmc h.lop i.mod j.jmc k.lop l.lop m.cnt n.cnt o.mlp p.ful q.jmc_ar r.ful s.ful t.mod u.mod v.cnt w.cnt x.ful y.cnt z.cnt"
     },
    "col":
    {"language": "Colombia",
        "axes": {
            "slnt": 18,
            "EXTD": 416,
            "SPED": 50
        },
     "UC":
     "A.cur B.dec C.cur D.dec E.cur F.cur G.dec H.cur I.cur J.cur K.cur L.dec M.cur N.cur O.cur P.dec Q.cur R.dec S.cur T.dec U.cur V.cur W.cur X.cur Y.cur Z.cur",
     "lc":
     "a.mod b.mlp c.mod d.mod e.ful f.mrr g.jmc h.lop i.mod j.jmc k.lop l.lop m.cnt n.cnt o.mlp p.jmc q.mrr r.ful s.ful t.mod u.mod v.cnt w.ful x.ful y.cnt z.mlp"
     },
}

tag = "arg"
print(lang_dict[tag])
