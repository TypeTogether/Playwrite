import sys
import os
from fontParts.world import *


def setFontInfo(font):
    font.info.styleName = "Guides"
    font.info.styleMapFamilyName = font.info.familyName + " Guides"
    psName = font.info.postscriptFontName.split("-")
    font.info.postscriptFontName = psName[0] + "Guides" + "-Regular"
    # font.features.text = font.features.text.replace(
    #     "(../features", "(../features")
    font.save()


def get_yGuides(font):
    was = font.info.openTypeOS2WinAscent
    capheight = font.info.capHeight
    xheight = font.info.xHeight
    baseline = 0
    descender = - font.info.openTypeOS2WinDescent

    return (capheight, xheight, baseline, descender)


def drawGuides(glyph, yValues, lineWidth=10):
    glyphWidth = glyph.width

    if glyph.name != ".notdef":
        glyph.clear(anchors=False)

    if glyphWidth and glyph.name != ".notdef":
        pen = glyph.getPen()
        for y in yValues:
            pen.moveTo((0, y))
            pen.lineTo((glyphWidth, y)),
            pen.lineTo((glyphWidth, y + lineWidth)),
            pen.lineTo((0, y + lineWidth)),
            pen.closePath()


def main():
    tag = sys.argv[1]
    tagnospace = tag.replace('_', '')
    src_path = os.path.abspath(f"./instance_ufo/Playpen{tagnospace}-Regular.ufo")
    tgt_path = src_path.replace("Regular", "Guides")

    src_font = OpenFont(src_path, showInterface=False)
    src_font.save(tgt_path)

    tgt_font = OpenFont(tgt_path, showInterface=False)
    setFontInfo(tgt_font)
    guides_y = get_yGuides(tgt_font)
    for glyph in tgt_font:
        drawGuides(glyph, guides_y)
    tgt_font.save()
    # save a copy for debug ufo
    tgt_font.save(os.path.expanduser("~/Desktop/debug.ufo"))


if __name__ == "__main__":
    main()
