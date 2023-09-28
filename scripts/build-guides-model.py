import sys
import os
from fontParts.world import *


def setFontInfo(font):
    font.info.styleName = "Guides"
    font.info.styleMapFamilyName = font.info.familyName + " Guides"
    psName = font.info.postscriptFontName.split("-")
    font.info.postscriptFontName = psName[0] + "Guides" + "-Regular"
    font.info.openTypeNameCompatibleFullName = font.info.styleMapFamilyName + " Regular"
    font.save()


def get_yGuides(font):
    was = font.info.openTypeOS2WinAscent
    # was = font.info.openTypeHheaAscender
    capheight = font.info.capHeight
    xheight = font.info.xHeight
    baseline = 0
    # descender = - font.info.openTypeOS2WinDescent
    descender = font.info.openTypeHheaDescender

    return (capheight, xheight, baseline, descender)


def drawGuides(glyph, yValues, lineWidth=19):

    x_min, x_max = 0, glyph.width
    if "cnct." in glyph.name:
        x_min, y_min, x_max, y_max = glyph.bounds

    if glyph.name != ".notdef" and x_min != x_max:
        glyph.decompose()
        pen = glyph.getPen()

        for y in yValues:
            if y == 0:
                line_width = lineWidth * 2
                shift = - line_width
            elif y < 0:
                line_width = lineWidth
                shift = - line_width
            else:
                line_width = lineWidth
                shift = 0

            # draw
            pen.moveTo((x_min, y + shift))
            pen.lineTo((x_max, y + shift)),
            pen.lineTo((x_max, y + shift + line_width)),
            pen.lineTo((x_min, y + shift + line_width)),
            pen.closePath()


def main():
    tag = sys.argv[1]
    tag_no_space = tag.replace("_", "")
    src_path = os.path.abspath(f"./instance_ufo/Playwrite{tag_no_space}-Regular.ufo")
    tgt_path = src_path.replace("Regular", "Guides")

    src_font = OpenFont(src_path, showInterface=False)
    src_font.save(tgt_path)

    tgt_font = OpenFont(tgt_path, showInterface=False)
    setFontInfo(tgt_font)
    guides_y = get_yGuides(tgt_font)

    for glyph in tgt_font:
        drawGuides(glyph, guides_y)
    tgt_font.save()

    # save a copy for debugging
    tgt_font.save(os.path.expanduser("~/Desktop/debug.ufo"))


if __name__ == "__main__":
    main()
