import sys
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from modelsData import modelsDataDict as mdd


def main():
    tags = sys.argv[1:]
    if "ALL" in tags:
        models_tags = mdd.keys()
    else:
        models_tags = [tag for tag in tags if tag in mdd.keys()]
    # build each
    for tag in models_tags:
        sl = mdd[tag]["slnt"]
        ex = mdd[tag]["EXTD"]
        sp = mdd[tag]["SPED"]
        varfont = TTFont(f"./../../fonts-models/fonts-{tag}/variable/Playpen{tag}[wght,EXTD,SPED,slnt].ttf")
        partial = instancer.instantiateVariableFont(varfont,
                                                    {
                                                        "wght": (100, 400),
                                                        "slnt": sl,
                                                        "EXTD": ex,
                                                        "SPED": sp
                                                    }
                                                    )
        # tag in output without "_"
        file_tag = tag.replace("_", "")
        partial.save(f"./../../fonts-models/fonts-{tag}/variable/Playpen{file_tag}[wght].ttf")
        partial.close()
        varfont.close()
        print(f"Instanced Playpen{file_tag}[wght].ttf")

if __name__ == "__main__":
    main()
