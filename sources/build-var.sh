# build Playwrite early variable

set -e

varFontsPath="../fonts/variable"
scripts="./scripts"

rm -rf $varFontsPath  # $ttfFontsPath $webFontsPath
mkdir -p $varFontsPath # $ttfFontsPath $webFontsPath

# pack source as .glyphspackage is not supported yet by fontmake
echo
echo "glyphspkg: Converting Playwrite_MM.glyphspackage to Playwrite_MM.glyphs"
glyphspkg Playwrite_MM.glyphspackage

echo "
==========================
 Generating VARIABLE font
==========================
 $(date "+ 📅 DATE: %Y-%m-%d%n  🕒 TIME: %H:%M:%S")"
echo

# Build variable font
fontmake -g ./Playwrite_MM.glyphs -o variable \
            --output-path $varFontsPath/Playwrite[wght,YEXT,SPED,slnt].ttf \
            --filter DecomposeTransformedComponentsFilter

# Post-processing?
