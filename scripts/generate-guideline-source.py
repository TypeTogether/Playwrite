import json
import glyphsLib
from pendot import create_effects, find_instance, transform_font
from glyphsLib.builder.transformations.propagate_anchors import propagate_all_anchors


font = glyphsLib.load("sources/Playwrite_MM.glyphspackage")
# Drop all masters and instances apart from ExtraLight (which we rename to Regular)
font.masters = [master for master in font.masters if master.weightValue == 100]
font.instances = [
    instance for instance in font.instances if instance.weightValue == 100
]

font.instances[0].name = "Regular"
font.instances[0].weight = 400

font.instances[1].name = "Italic"
font.instances[1].weight = 400
font.instances[1].linkStyle = "Regular"


propagate_all_anchors(font)

for glyph in font.glyphs:
    if "comb" in glyph.name:
        glyph.userData["co.uk.corvelsoftware.Dotter.disableGuidelines"] = True
    elif glyph.name in ["space", "nbspace", "CR", ".notdef", "thinspace"]:
        glyph.userData["co.uk.corvelsoftware.Dotter.disableGuidelines"] = True
    elif glyph.name == "underscore":
        glyph.userData["co.uk.corvelsoftware.Dotter.disableCopy"] = True
    # Restrict layers to existing masters
    glyph.layers = [
        layer
        for layer in glyph.layers
        if layer.layerId in [master.id for master in font.masters]
    ]

with open("sources/guidelines.json") as f:
    overrides = json.load(f)
effects = create_effects(font, None, overrides)
transform_font(font, effects)

font.familyName = "Playwrite Guides"
font.featurePrefixes["Languagesystems"].code = font.featurePrefixes[
    "Languagesystems"
].code.replace("include(features", "include(../features")
font.save("sources/generated/Playwrite-Guides.glyphs")
