# make ufo masters from glyphs file

set -e

ufoFolder="./sources-ufo"

echo
echo "glyphspkg: Converting Playpen_MM.glyphspackage to Playpen_MM.glyphs"
glyphspkg Playpen_MM.glyphspackage


ufoFolder="./sources-ufo"

python -m glyphsLib glyphs2ufo Playpen_MM.glyphs -m $ufoFolder \
		--write-public-skip-export-glyphs \
		--no-store-editor-state
		# --normalize-ufos \
		# --ufo-module defcon

python ./scripts/write-fea-to-ufo-models.py
