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
        tagnospace = tag.replace("_", "")
        sl = mdd[tag]["slnt"]
        ex = mdd[tag]["EXTD"]
        sp = mdd[tag]["SPED"]
        varfont = TTFont(f"./../../fonts-models/fonts-{tag}/variable/Playpen{tagnospace}[wght,EXTD,SPED,slnt].ttf")
        # fix hasItalics (ENG_Joined and Semijoined by now)
        has_sl = ""
        if type(sl) is str and "-" in sl:
            min_sl, max_sl = sl.split("-")
            sl = (int(min_sl), int(max_sl))
            has_sl = ",slnt"
        var_wght_only = instancer.instantiateVariableFont(varfont,
                                                    {
                                                        "wght": (100, 400),
                                                        "slnt": sl,
                                                        "EXTD": ex,
                                                        "SPED": sp
                                                    }
                                                    )
        # fix post italic Angle
        if sl != 0 and type(sl) != tuple:
            var_wght_only["post"].italicAngle = - int(sl)
        # tag in output without "_"
        var_wght_only.save(f"./../../fonts-models/fonts-{tag}/variable/Playpen{tagnospace}[wght{has_sl}].ttf")
        var_wght_only.close()
        varfont.close()
        print(f"Instanced Playpen{tagnospace}[wght{has_sl}].ttf")

if __name__ == "__main__":
    main()
