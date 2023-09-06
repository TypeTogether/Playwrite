# build Playpen fonts

set -e

otfFontsPath="../fonts/static/otf"
ttfFontsPath="../fonts/static/ttf"
webFontsPath="../fonts/static/web"
scripts="./scripts"

rm -rf $ttfFontsPath # $otfFontsPath $webFontsPath
mkdir -p $ttfFontsPath # $otfFontsPath $webFontsPath

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

# # Build OTF fonts
# fontmake -g ./Playpen_MM.glyphs -i -o otf --output-dir $otfFontsPath

# Build TTF fonts
fontmake -g ./Playpen_MM.glyphs -i -o ttf --output-dir $ttfFontsPath \
          --filter DecomposeTransformedComponentsFilter \
          --flatten-components

# echo "
# ======================
#  Post processing OTFs 
# ======================
# "
# otfs=$(ls $otfFontsPath/*.otf)
# for otf in $otfs
# do
#     echo $otf
#     python $scripts/fix-usWeightClass-otf.py $otf
#     # psautohint --no-zones-stems -a $otf
# done

echo "
======================
 Post processing TTFs 
======================
"
ttfs=$(ls $ttfFontsPath/*.ttf)
for ttf in $ttfs
do
  python -m ttfautohint $ttf "$ttf.hint"
  mv "$ttf.hint" $ttf
  gftools fix-hinting $ttf
  echo $ttf
done

# Clean up
rm -rf ./master_ufo/ ./instance_ufo/
