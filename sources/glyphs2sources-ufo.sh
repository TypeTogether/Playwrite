# make ufo masters from glyphs file

set -e

echo
echo "glyphspkg: Converting Playpen_MM.glyphspackage to Playpen_MM.glyphs"
glyphspkg Playpen_MM.glyphspackage


ufoFolder="./sources-ufo"

python3 -m glyphsLib glyphs2ufo Playpen_MM.glyphs -m $ufoFolder \
		--write-public-skip-export-glyphs \
		--no-store-editor-state \
		--normalize-ufos \
		--ufo-module defcon
