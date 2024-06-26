# add tag.fea to `locl` include

__doc__ = """
    Adds 'tag.fea' to include in `locl` feature.
"""

import sys
import os

tag, feaFilepath = sys.argv[1], sys.argv[2]

# print(f"Building {tag.upper()} fonts")
print(f"Building {tag} fonts")

feaTagFilepath = feaFilepath.replace(".fea", "-temp.fea")

with open(feaFilepath, "r") as fea:
    fea_text = fea.read()
    fea_temp = fea_text.replace("::TAG::", tag)


with open(feaTagFilepath, "w") as featemp:
    featemp.write(fea_temp)
    featemp.close()
