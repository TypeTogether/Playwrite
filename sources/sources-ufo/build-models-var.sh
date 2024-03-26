# build Playwrite variable fonts per country

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
    python $scripts/build-wght-only-model-var.py $tag
done
