# build Playwrite variable fonts per country

set -e


scripts="../scripts"
feaFile=../features/Playwrite-models.fea

if [ $1 = "ALL" ]; then
    models=( ARG AUS_NSW AUS_QLD AUS_SA AUS_TAS AUS_VIC AUT BEL_VLG BEL_WAL BRA CAN CHI COL CUB CZE DEU_Grundschrift DEU_LA DEU_SAS DEU_VA DNK_Looped DNK_Unlooped ENG_Joined ENG_Semijoined ESP ESP_OrnateUC EST FRA_Modern FRA_Traditional HRV HRV_Lefthand HUN IDN IND IRL ISL ITA_Modern ITA_Traditional MEX NLD NOR NZL PER POL PRT ROU SVK TZA USA_Modern USA_Traditional VNM ZAF )
else
    models=( "$@" )
fi

args=()
for i in "${models[@]}"
do
    echo
    echo "================================================"
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
    tag_no_space=${tag/"_"/""}
    varFileName="Playwrite$tag_no_space[wght,YEXT,SPED,slnt].ttf"
    tempVarFileName="var-model-temp.ttf"
    temp_ttf=$varFontsPath/$tempVarFileName
    # Build VAR font for model
    fontmake -m ./designspace-models/$tag.designspace \
            -o variable \
            --output-path $temp_ttf \
            --filter DecomposeTransformedComponentsFilter \
            --expand-features-to-instances

    echo "
  =====================
   Post processing VAR
  =====================
  "
    ttf=$varFontsPath/$varFileName
    # add STAT, rename, autohint
    gftools gen-stat $temp_ttf --src config.yaml --inplace
    mv $temp_ttf $ttf
    # python -m ttfautohint -n $ttf "$ttf.hint"
    # mv "$ttf.hint" $ttf
    # gftools fix-hinting $ttf
    # mv "$ttf.fix" $ttf
    gftools fix-nonhinting $ttf $ttf
    # fix var name table
    python $scripts/fix-var-model-name.py $tag $ttf
    echo $ttf
    rm $varFontsPath/*gasp*

    echo "
  =====================
   Building [wght] VAR
  =====================
  "
    # Build [wght] only variable for model
    python $scripts/build-wght-model-var.py $tag
done
