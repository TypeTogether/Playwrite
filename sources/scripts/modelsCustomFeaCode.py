__doc__ = """
    This file contains a dictionary with custom code for specific models to be included in the MODEL fea that will be later also included in the locl feature as a dictionary.
    It's manually mantained.
"""

modelsCustomFeaCodeDict = {
    # "TAG": "fea code"
    "CZE": "sub caroncomb.alt by caroncomb.alt_locl;\nsub caroncomb by caroncomb_locl;",
    "SVK": "sub caroncomb.alt by caroncomb.alt_locl;\nsub caroncomb by caroncomb_locl;",
    "ESP": "sub [l l.mod l.lop L L.cur L.dec] periodcentered' by dotaccentcomb.CAT;",
    "ESP_OrnateUC": "sub [l l.mod l.lop L L.cur L.dec] periodcentered' by dotaccentcomb.CAT;",
    "NLD": "sub i.mod j.jmc by ij.jmc;",
    "ROU": "sub [S.dec T.dec s.ful t.mod] commaaccentcomb' by cedillacomb;"
}
