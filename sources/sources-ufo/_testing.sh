# testing bits of code

tag="col"
feaFile="../features/Playpen-models.fea"

scripts="../scripts"

# set right tag to fea
python $scripts/add-locl-fea.py $tag $feaFile



# ------------------
# # echo $@

# for i in $@
# do
#     echo "tag: $i"
# done


