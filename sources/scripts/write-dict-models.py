# write-models-dict

__doc__ = """
    Write a python dictionary with the data read from "models-all.csv" file for later import.
    Saves "modelsData.py" file in the same "scripts" folder with a dictionary named *modelsDataDict*.
    Import code should look like:
    `from modelsData import modelsDataDict`
"""


import pprint


with open("../data/models-all.csv", "r") as csv:
    models_dict = {}
    headers = csv.readline()[:-1].split(";")
    country, tag, slnt, yext, sped, uppercase, lowercase = headers
    lines = csv.readlines()
    for line in lines:
        # remove newline
        line = line[:-1]
        # print(line)
        c, t, sl, e, sp, u, l, = line.split(";")
        try:
            models_dict[t] = {
                country: c,
                slnt: -int(sl),
                yext: int(e),
                sped: int(sp),
                uppercase: u,
                lowercase: l,
            }
        except ValueError:
            if "-" in sl:
                print(f" ⚠️  {t} has a range for slnt axis (has italic)")
                models_dict[t] = {
                    country: c,
                    slnt: sl,
                    yext: int(e),
                    sped: int(sp),
                    uppercase: u,
                    lowercase: l,
            }
    csv.close()

with open("modelsData.py", "w") as d:
    # pprint.pprint(models_dict, d)
    pretty = pprint.pformat(models_dict)
    all_txt = f"modelsDataDict = {pretty}"
    d.write(all_txt)
    d.close()

print(" 💾 modelsData.py file")
