# build Playwrite fonts per country

set -e

scripts="../scripts"
feaFile=../features/Playwrite-models.fea

if [ $1 = "ALL" ]; then
    models=( ARG AUS_NSW AUS_QLD AUS_SA AUS_TAS AUS_VIC BEL_VLG BEL_WAL BRA CAN CHI COL CUB CZE DEU_Grundschrift DEU_LA DEU_SAS DEU_VA DNK_Looped DNK_Unlooped ENG_Joined ENG_Semijoined ESP ESP_OrnateUC FRA_Modern FRA_Traditional HRV HRV_Lefthand IDN IRL ISL ITA_Modern ITA_Traditional MEX NLD NOR NZL PER POL PRT SVK USA_Modern USA_Traditional VNM ZAF )
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
    tagnospace=${tag/"_"/""}
    fontmake -m ./designspace-models/$tag.designspace -i "Playwrite $tagspaced Thin" -o ufo \
    # save as Guides ufo and process
    python $scripts/build-guides-model.py $tag

    fontmake -u ./instance_ufo/Playwrite$tagnospace-Guides.ufo -o ttf \
            --output-dir $ttfFontsPath \
            --filter DecomposeTransformedComponentsFilter \
            --fea-include-dir ../features

    echo "
    =====================
     Post processing TTF
    =====================
    "
    ttf=$ttfFontsPath/Playwrite$tagnospace-Guides.ttf
    echo $ttf
    python -m ttfautohint -n $ttf "$ttf.hint"
    mv "$ttf.hint" $ttf
    gftools fix-hinting $ttf
    mv "$ttf.fix" $ttf
    echo $ttf
done
