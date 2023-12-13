import sys
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from modelsData import modelsDataDict as mdd
import subprocess

# Dirty procedural code

def fix_italic_variable(font, find_, replace_):
    IDS_FIX = [2, 3, 4, 6]

    name_table = font["name"]
    for name_record in name_table.names:
        if name_record.nameID in IDS_FIX:
            old = name_record.toUnicode()
            new = old.replace(find_, replace_)
            if old != new:
                name_record.string = new
        # append "varItalic" to id 25
        elif name_record.nameID == 25:
            name_record.string = old.split('-')[0] + "varItalic"


def main():
    tags = sys.argv[1:]

    if "ALL" in tags:
        models_tags = mdd.keys()
    else:
        models_tags = [tag for tag in tags if tag in mdd.keys()]

    # build each
    for tag in models_tags:
        tag_no_space = tag.replace("_", "")
        sl = mdd[tag]["slnt"]
        ex = mdd[tag]["YEXT"]
        sp = mdd[tag]["SPED"]
        varfont = TTFont(f"./../../fonts-models/fonts-{tag}/variable/Playwrite{tag_no_space}[wght,YEXT,SPED,slnt].ttf")

        # fix hasItalics (ENG_Joined and Semijoined by now)
        has_italic = False
        if type(sl) is str and "-" in sl:
            min_sl, max_sl = sl.split("-")
            sl = (int(min_sl), int(max_sl))
            has_italic = True

        if has_italic is False:
            var_wght_only = instancer.instantiateVariableFont(varfont,
                                                              {
                                                                  "wght": (100, 400),
                                                                  "slnt": sl,
                                                                  "YEXT": ex,
                                                                  "SPED": sp
                                                              }
                                                              )

            # fix post italicAngle and caret slopes
            var_wght_only["post"].italicAngle = 0
            var_wght_only["hhea"].caretSlopeRise = 1
            var_wght_only["hhea"].caretSlopeRun = 0

            # fix hhea table
            var_wght_only["hhea"].ascender = var_wght_only[
                "OS/2"].sTypoAscender
            var_wght_only["hhea"].descender = var_wght_only[
                "OS/2"].sTypoDescender

            # tag in output without "_"
            var_wght_only.save(f"./../../fonts-models/fonts-{tag}/variable/Playwrite{tag_no_space}[wght].ttf")
            var_wght_only.close()

            print(f"Instanced Playwrite{tag_no_space}[wght].ttf")

        else:
            for slant_val in sl:
                var_wght_only = instancer.instantiateVariableFont(varfont,
                                                                  {
                                                                      "wght": (100, 400),
                                                                      "slnt": slant_val,
                                                                      "YEXT": ex,
                                                                      "SPED": sp
                                                                  }
                                                                  )
                # fix hhea ascender/descender
                var_wght_only["hhea"].ascender = var_wght_only[
                    "OS/2"].sTypoAscender
                var_wght_only["hhea"].descender = var_wght_only[
                    "OS/2"].sTypoDescender

                # fix tables
                if slant_val == 0:
                    italic = ""
                    var_wght_only["post"].italicAngle = 0
                    var_wght_only["hhea"].caretSlopeRise = 1
                    var_wght_only["hhea"].caretSlopeRun = 0
                else:
                    italic = "-Italic"
                    var_wght_only["post"].italicAngle = - slant_val
                    var_wght_only["hhea"].caretSlopeRise = 1000
                    var_wght_only["hhea"].caretSlopeRun = 231
                    var_wght_only['head'].macStyle = 2
                    var_wght_only['OS/2'].fsSelection = 385

                    fix_italic_variable(var_wght_only, "Regular", "Italic")
                    # var_wght_only["name"].setName(string="Italic",  nameID=2,
                    #                        platformID=3, platEncID=1, langID=0x409)

    # if "Italic" in file.split("-")[-1].split(".")[0]:
    #     newNameID1 = ttFont["name"].getDebugName(1).replace(" Italic", "")

    #     ttFont["name"].setName(string=newNameID1,  nameID=1,
    #                            platformID=3, platEncID=1, langID=0x409)

    #     ttFont["name"].setName(string="Italic",  nameID=2,
    #                            platformID=3, platEncID=1, langID=0x409)

                # tag in output without "_"
                output_path = f"./../../fonts-models/fonts-{tag}/variable/Playwrite{tag_no_space}{italic}[wght].ttf"
                var_wght_only.save(output_path)
                var_wght_only.close()

                # fix stat table if has italics
                stat_file = "./../sources-ufo/config-hasItalic.yaml"

                fix_it_stat = subprocess.run(
                    ['gftools', 'gen-stat', output_path, '--src', stat_file, '--inplace'], stdout=subprocess.PIPE)

                print(f"Instanced Playwrite{tag_no_space}{italic}[wght].ttf")
                print(fix_it_stat.stdout.decode())

        varfont.close()

if __name__ == "__main__":
    main()
