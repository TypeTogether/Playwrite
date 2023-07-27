# Write fea to ufo models

__doc__ = """
    Write the include statement to models ufo sources
"""


import os
from fontParts.world import *

folder_ufos = "./sources-ufo"
fea_code = """languagesystem DFLT dflt;
languagesystem latn dflt;

include(../features/Playpen-models-temp.fea);

"""

ufo_files = [os.path.join(folder_ufos, ufo) for ufo in os.listdir(folder_ufos) if ufo.endswith(".ufo") is True]

for ufo_path in ufo_files:
    font = OpenFont(ufo_path, showInterface=False)
    font.features.text = fea_code
    font.save()
    font.close()

print("Written .fea include code to source ufos")
