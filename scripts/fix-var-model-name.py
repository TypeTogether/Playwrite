import sys
import os
from fontTools.ttLib import TTFont


__doc__ = """
Fix `name` table for model variable font.
Arguments: tag variableFontPath
"""


def getFontNameID(font, ID, platformID=3, platEncID=1):

    name = str(font['name'].getName(ID, platformID, platEncID))
    return name


def setFontNameID(font, ID, newName):
    winIDs = {"platformID": 3, "platEncID": 1, "langID": 0x409}
    # macIDs = {"platformID": 1, "platEncID": 0, "langID": 0x0}

    oldWinName = font['name'].getName(ID, *winIDs.values())
    font['name'].setName(newName, ID, *winIDs.values())


def main():

    tag, fpath = sys.argv[1], sys.argv[2]
    tag_no_space = tag.replace("_", "")
    tag_space = tag.replace("_", " ")
    font = TTFont(fpath)

    # ID 1: Family Name
    setFontNameID(font, 1, f"Playwrite {tag_space}")

    # ID 3: Unique Font Identifier
    id3 = getFontNameID(font, 3)
    new_id3 = id3.split(";")[:-1] + [f"Playwrite{tag_no_space}-Regular"]
    setFontNameID(font, 3, f"{';'.join(new_id3)}")

    # ID 4: Full Font Name
    setFontNameID(font, 4, f"Playwrite {tag_space} Regular")

    # ID 6 Postscript Font Name:
    setFontNameID(font, 6, f"Playwrite{tag_no_space}-Regular")

    # ID 16 and 17: Typographic Family and SubFamily Name
    font['name'].removeNames(nameID=16)
    font['name'].removeNames(nameID=17)

    # ID 25 Variations Postscript prefix
    setFontNameID(font, 25, f"Playwrite{tag_no_space}var")

    font.save(fpath)
    font.close()


if __name__ == "__main__":

    main()
