# build Playpen fonts per country

set -e

scripts="../scripts"
feaFile=../features/Playpen-models.fea

if [ $1 = "ALL" ]; then
    models=( ARG AUS_NSW AUS_QLD AUS_SA AUS_TAS AUS_VIC BEL_VLG BEL_WAL BRA CAN CHI COL CUB CZE DEU_Grundschrift DEU_LA DEU_SAS DEU_VA DNK_Looped DNK_Unlooped ENG_Joined ENG_Semijoined ESP ESP_OrnateUC FRA_Modern FRA_Traditional HRV HRV_Lefthand IDN IRL ISL ITA_Modern ITA_Traditional MEX NLD NOR NZL PER POL POR SVK USA_Modern USA_Traditional VNM ZAF )
else
    models=( "$@" )
fi

args=()
for i in "${models[@]}"
do
    echo
    args+=(--filter="+ $i")
    echo "tag: $i"
    tag=$i

    ttfFontsPath="../../fonts-models/fonts-$tag/static/ttf"

    rm -rf $ttfFontsPath  # $ttfFontsPath $webFontsPath
    mkdir -p $ttfFontsPath # $ttfFontsPath $webFontsPath

    # set locl code in features
    python $scripts/add-locl-fea.py $tag $feaFile

    echo "
================================================
 Generating STATIC **$tag** fonts
================================================
 $(date "+ 📅 DATE: %Y-%m-%d%n  🕒 TIME: %H:%M:%S")"
echo

    # Build TTF fonts
    fontmake -m ./designspace-models/$tag.designspace -i -o ttf \
            --output-dir $ttfFontsPath \
            --filter DecomposeTransformedComponentsFilter \
            --expand-features-to-instances
            # --flatten-components

    echo "
    ===============================
     Building GUIDES **$tag** font
    ===============================
    "
    # python $scripts/build-guides-model.py $tag
    sh build-models-guides-static.sh **$tag**

    echo "
    ======================
     Post processing TTFs 
    ======================
    "
    ttfs=$(ls $ttfFontsPath/*.ttf)
    for ttf in $ttfs
    do
      python -m ttfautohint -n $ttf "$ttf.hint"
      mv "$ttf.hint" $ttf
      gftools fix-hinting $ttf
      mv "$ttf.fix" $ttf
      echo $ttf
      # fix post.italicAngle
      python $scripts/fix-models-static.py $ttf
    done
done

#
open "../../test/test-models.gggls"
