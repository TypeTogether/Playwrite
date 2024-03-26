__doc__ = """
    This file contains a dictionary with custom code for specific models to be included in the MODEL fea that will be later also included in the locl feature as a dictionary.
    It's manually mantained.
"""

modelsCustomFeaCodeDict = {
    # "TAG": "fea code"
    "CZ": "sub caroncomb.alt by caroncomb.alt_locl;\nsub caroncomb by caroncomb_locl;",
    "SK": "sub caroncomb.alt by caroncomb.alt_locl;\nsub caroncomb by caroncomb_locl;",
    "ES": "sub [l l.mod l.lop L L.cur L.dec] periodcentered' by dotaccentcomb.CAT;",
    "ES_Deco": "sub [l l.mod l.lop L L.cur L.dec] periodcentered' by dotaccentcomb.CAT;",
    "NL": "sub i.mod j.jmc by ij.jmc;",
    "RO": "sub [S S.cur S.dec] cedillacomb.case' by commaaccentcomb.case\nsub [s s.mod s.jmc s.ful s.mlp] cedillacomb' by commaaccentcomb;"
}
