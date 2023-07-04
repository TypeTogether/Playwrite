# build Playpen early variable

set -e

varFontsPath="../fonts/variable"
scripts="./scripts"

rm -rf $varFontsPath  # $ttfFontsPath $webFontsPath
mkdir -p $varFontsPath # $ttfFontsPath $webFontsPath

# pack source as .glyphspackage is not supported yet by fontmake
echo
echo "glyphspkg: Converting Playpen_MM.glyphspackage to Playpen_MM.glyphs"
glyphspkg Playpen_MM.glyphspackage

echo "
=========================
 Generating STATIC fonts
=========================
 $(date "+ 📅 DATE: %Y-%m-%d%n  🕒 TIME: %H:%M:%S")"
echo

# Build variable font
fontmake -g ./Playpen_MM.glyphs -o variable --output-dir $varFontsPath \
          --filter DecomposeTransformedComponentsFilter

# Clean up
rm -rf ./master_ufo/ ./instance_ufo/
