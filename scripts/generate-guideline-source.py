import json
import glyphsLib
from pendot import create_effects, find_instance, transform_font
from glyphsLib.builder.transformations.propagate_anchors import propagate_all_anchors


font = glyphsLib.load("sources/Playwrite_MM.glyphspackage")

propagate_all_anchors(font)

for glyph in font.glyphs:
    if "comb" in glyph.name:
        glyph.userData["co.uk.corvelsoftware.Dotter.disableGuidelines"] = True
    elif glyph.name in ["space", "nbspace", "CR", ".notdef", "thinspace"]:
        glyph.userData["co.uk.corvelsoftware.Dotter.disableGuidelines"] = True
    elif glyph.name == "underscore":
        glyph.userData["co.uk.corvelsoftware.Dotter.disableCopy"] = True

with open("sources/guidelines.json") as f:
    overrides = json.load(f)
effects = create_effects(font, None, overrides)
transform_font(font, effects)

font.familyName = "Playwrite Guides"
font.featurePrefixes["Languagesystems"].code = font.featurePrefixes[
    "Languagesystems"
].code.replace("include(features", "include(../features")
font.save("sources/generated/Playwrite-Guides.glyphs")
