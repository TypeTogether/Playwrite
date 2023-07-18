# build Playpen fonts per country

set -e

# # keep running if fontmake has an error
# fontmake || true

scripts="../scripts"
feaFile=../features/Playpen-models.fea

if [ $1 = "ALL" ]; then
    # models=( AUS_QLD IRL ISL )
    models=( ARG AUS_NSW AUS_QLD AUS_SA AUS_TAS AUS_VIC BRA CAN CHI COL CUB CZE DEU_Grundschrift DEU_LA DEU_SAS DEU_VA DNK_Looped DNK_Unlooped ESP_OrnateUC ESP FRA_Modern FRA_Traditional HRV_Lefthand HRV IDN IRL ISL ITA_Modern ITA_Traditional MEX NLD NOR PER POL POR SVK USA_Modern USA_Traditional VNM )
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

    otfFontsPath="../../fonts-models/fonts-$tag/static/otf"
    # ttfFontsPath="../fonts/static/ttf"
    # webFontsPath="../fonts/static/web"

    rm -rf $otfFontsPath  # $ttfFontsPath $webFontsPath
    mkdir -p $otfFontsPath # $ttfFontsPath $webFontsPath

    # set locl code in features
    python $scripts/add-locl-fea.py $tag $feaFile

    echo "
==================================
 Generating STATIC **$tag** fonts
==================================
$(date "+ 📅 DATE: %Y-%m-%d%n  🕒 TIME: %H:%M:%S")"
    echo

    # Build OTF fonts
    fontmake -m ./designspace-models/$tag.designspace -i -o otf \
                --output-dir $otfFontsPath \
                --expand-features-to-instances

    # # Build TTF fonts
    # fontmake -g ./Playpen_MM.glyphs -i -o ttf --output-dir $ttfFontsPath \
    #           --filter DecomposeTransformedComponentsFilter \
    #           --flatten-components

    # echo "
    # ======================
    #  Post processing OTFs 
    # ======================
    # "
    # otfs=$(ls $otfFontsPath/*.otf)
    # for otf in $otfs
    # do
    #   echo $otf
    #   python $scripts/fix-usWeightClass-otf.py $otf
    #   psautohint --no-zones-stems -a $otf
    # done

    # echo "
    # ======================
    #  Post processing TTFs 
    # ======================
    # "
    # ttfs=$(ls $ttfFontsPath/*.ttf)
    # for ttf in $ttfs
    # do
    #   ttfautohint $ttf "$ttf.hint"
    #   mv "$ttf.hint" $ttf
    #   gftools fix-hinting $ttf;
    #   mv "$ttf.fix" $ttf;
    #   echo $ttf
    #   sfnt2woff $ttf
    #   woff2_compress $ttf
    #   lenght=${#ttf}
    #   echo "Compressing to .woff:"
    #   mv ${ttf:0:$lenght-4}.woff $webFontsPath
    #   mv ${ttf:0:$lenght-4}.woff2 $webFontsPath
    # done

    # Clean up
    rm -rf ./master_ufo/ ./instance_ufo/
done

