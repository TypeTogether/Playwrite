# build Playpen variable fonts per country

set -e


scripts="../scripts"
feaFile=../features/Playpen-models.fea

if [ $1 = "ALL" ]; then
    models=( ARG AUS_NSW AUS_QLD AUS_SA AUS_TAS AUS_VIC BEL_VLG BEL_WAL BRA CAN CHI COL CUB CZE DEU_Grundschrift DEU_LA DEU_SAS DEU_VA DNK_Looped DNK_Unlooped ESP ESP_OrnateUC FRA_Modern FRA_Traditional HRV HRV_Lefthand IDN IRL ISL ITA_Modern ITA_Traditional MEX NLD NOR NZL PER POL POR SVK USA_Modern USA_Traditional VNM ZAF )
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

    varFontsPath="../../fonts-models/fonts-$tag/variable"

    rm -rf $varFontsPath
    mkdir -p $varFontsPath

    # set locl code in features
    python $scripts/add-locl-fea.py $tag $feaFile

    echo "
================================================
 Generating VARIABLE **$tag** font
================================================
 $(date "+ 📅 DATE: %Y-%m-%d%n  🕒 TIME: %H:%M:%S")"
echo

    # temporal file name (referenced in config.yaml for STAT):
    varFileName="Playpen$tag[wght,EXTD,SPED,slnt].ttf"
    tempVarFileName="var-model-temp.ttf"
    temp_ttf=$varFontsPath/$tempVarFileName
    # Build VAR font for model
    fontmake -m ./designspace-models/$tag.designspace \
            -o variable \
            --output-path $temp_ttf \
            --filter DecomposeTransformedComponentsFilter \
            --expand-features-to-instances

    echo "
    ======================
     Post processing VAR
    ======================
    "
    # ttfs=$(ls $varFontsPath/*.ttf)
    # for ttf in $ttfs
    # do
    ttf=$varFontsPath/$varFileName
    # add STAT, rename, autohint
    gftools gen-stat $temp_ttf --src config.yaml --inplace
    mv $temp_ttf $ttf
    python -m ttfautohint $ttf "$ttf.hint"
    mv "$ttf.hint" $ttf
    echo $ttf
    # done

    # Clean up for each model
    rm -rf ./master_ufo/ ./instance_ufo/
done

#
open "../../test/test-var-models.gggls"
