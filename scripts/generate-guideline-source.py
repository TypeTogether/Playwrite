import glyphsLib

font = glyphsLib.load("sources/Playwrite_MM.glyphspackage")
for glyph in font.glyphs:
    if glyph.name.endswith("comb"):
        glyph.userData["co.uk.corvelsoftware.Dotter.disableGuidelines"] = True
    if glyph.name in ["space", "nbspace"]:
        glyph.userData["co.uk.corvelsoftware.Dotter.disableGuidelines"] = True
    if glyph.name == "underscore":
        glyph.userData["co.uk.corvelsoftware.Dotter.disableCopy"] = True
font.save("sources/generated/Playwrite.glyphs")
