# build Playwrite fonts per country

set -e

scripts="../scripts"
feaFile=../features/Playwrite-models.fea

if [ $1 = "ALL" ]; then
    models=( AR AU_NSW AU_QLD AU_SA AU_TAS AU_VIC AT BE_WAL BE_VLG BR CA CL CO HR HR_Lijeva CU CZ DK_Loopet DK_Uloopet EE GB_S GB_J FR_Trad FR_Moderne DE_Grund DE_LA DE_SAS DE_VA HU IS IN ID IE IT_Trad IT_Moderna MX NL NZ NG_Modern NO PE PL PT RO SK ZA ES ES_Deco TZ US_Modern US_Trad VN )
else
    models=( "$@" )
fi

args=()
for i in "${models[@]}"
do
    # echo
    args+=(--filter="+ $i")
    # echo "tag: $i"
    tag=$i

    ttfFontsPath="../../fonts-models/fonts-$tag/static/ttf"

    mkdir -p $ttfFontsPath

    # set locl code in features
    python $scripts/add-locl-fea.py $tag $feaFile

    echo "
================================================
 Generating STATIC **$tag** GUIDES font
================================================
 $(date "+ 📅 DATE: %Y-%m-%d%n  🕒 TIME: %H:%M:%S")"
echo

    # Build Thin instance ufo
    tagspaced=${tag/"_"/" "}
    tag_no_space=${tag/"_"/""}
    fontmake -m ./designspace-models/$tag.designspace -i "Playwrite $tagspaced Regular" -o ufo \
    # save as Guides ufo and process
    python $scripts/build-guides-model.py $tag

    fontmake -u ./instance_ufo/Playwrite$tag_no_space-Guides.ufo -o ttf \
            --output-dir $ttfFontsPath \
            --filter DecomposeTransformedComponentsFilter \
            --fea-include-dir ../features

    echo "
    =====================
     Post processing TTF
    =====================
    "
    ttf=$ttfFontsPath/Playwrite$tag_no_space-Guides.ttf
    echo $ttf
    python -m ttfautohint -n $ttf "$ttf.hint"
    mv "$ttf.hint" $ttf
    gftools fix-hinting $ttf
    mv "$ttf.fix" $ttf
    echo $ttf
done

# clean-up
rm -rf ./instance_ufo
