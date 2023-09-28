# Construct a builder config file from the data in data/models-all.csv
import csv
import yaml
import copy

config = {
    "sources": ["Playpen_MM.glyphspackage"],
    "recipe": {
        "../fonts/variable/Playpen_MM[SPED,YEXT,slnt,wght].ttf": [
            {"source": "Playpen_MM.glyphspackage"},
            {
                "operation": "buildVariable",
                "fontmake_args": "--no-production-names --filter ... --filter FlattenComponentsFilter --filter DecomposeTransformedComponentsFilter",
            },
        ]
    },
}

STATICS = {
    "Thin": 100,
    "ExtraLight": 200,
    "Light": 300,
    "Regular": 400,
}

def to_italic(name):
    if name == "Regular":
        return "Italic"
    else:
        return name+"Italic"

UC_ORDER = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "U+00C6",
    "U+00D0",
    "U+0132",
    "U+014a",
    "U+0152",
    "U+00DE",
    "U+1E9E",
]
LC_ORDER = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "U+00E6",
    "U+00F0",
    "U+0133",
    "U+014B",
    "U+0153",
    "U+00FE",
    "U+00DF",
    "U+0131",
    "U+0237",
]


def get_mapping(model):
    # There are UC/LC mappings in the models-all file, but they're WRONG!
    new_ucs = model["UC"].split(" ")
    new_lcs = model["lc"].split(" ")
    # We have to look in the feature files instead.

    mapping = {}
    feafile = "features/fea-models/" + model["lang_tag"] + ".fea"
    # They won't parse, since they're snippets, so we use a hacky workaround
    # with open(feafile, "r") as file:
    #     for line in file:
    #         if line.startswith("@UC_"+model["lang_tag"]):
    #             new_ucs = line.split(" = ")[1][1:-2].split(" ")
    #         if line.startswith("@lc_"+model["lang_tag"]):
    #             new_lcs = line.split(" = ")[1][1:-2].split(" ")
    # assert new_ucs and new_lcs, "Couldn't find UC/LC mappings in " + feafile
    for old, new in zip(UC_ORDER, new_ucs):
        mapping[old] = new
    for old, new in zip(LC_ORDER, new_lcs):
        mapping[old] = new

    return mapping


with open("sources/data/models-all.csv", "r") as file:
    reader = csv.DictReader(file, delimiter=";")
    for ix,model in enumerate(reader):
        model_name = model["Country"]
        if "_" in model["lang_tag"]:
            model_name += " " + model["lang_tag"].split("_")[1]
        file_name = model_name.replace(" ", "")
        if "-" in model['slnt']:
            axes = "slnt,wght"
        else:
            axes = "wght"
        subspace = f"YEXT={model['YEXT']} SPED={model['SPED']} slnt={model['slnt'].replace('-',':')}"
        output = "../fonts/variable/Playpen" + file_name + f"[{axes}].ttf"
        steps = copy.deepcopy(
            config["recipe"]["../fonts/variable/Playpen_MM[SPED,YEXT,slnt,wght].ttf"]
        )
        steps.append(
            {
                "operation": "subspace",
                "axes": subspace,
            }
        )
        steps.append({"operation": "remap", "mappings": get_mapping(model)})
        # steps.append({"operation": "hbsubset"})
        # steps.append({"operation": "fix"})
        steps.append({"operation": "rename", "name": "Playpen " + model_name})
        stat_file = "stat.yaml"
        if "-" in model['slnt']:
            stat_file = "stat-italic.yaml"
        steps.append({"operation": "buildStat", "other_args": "--src "+stat_file})
        config["recipe"][output] = steps

        # # And now for statics
        for style, wght in STATICS.items():
            output = f"../fonts/static/{file_name}/Playpen{file_name}-{style}.ttf"
            if "-" in model['slnt']:
                low, high = [int(x) for x in model['slnt'].split("-")]
                lowsteps = copy.deepcopy(steps)
                lowsteps.append(
                    {
                        "operation": "subspace",
                        "axes": f"wght={wght} slnt={low}",
                    }
                )
                lowsteps.append({"postprocess": "fix", "fixargs": "--include-source-fixes"})
                config["recipe"][output] = lowsteps
                highsteps = copy.deepcopy(steps)
                highsteps.append(
                    {
                        "operation": "subspace",
                        "axes": f"wght={wght} slnt={high}",
                        "other_args": "--update-name-table"
                    }
                )
                highsteps.append({"postprocess": "fix", "fixargs": "--include-source-fixes"})
                italic_output = f"../fonts/static/{file_name}/Playpen{file_name}-{to_italic(style)}.ttf"
                config["recipe"][italic_output] = highsteps
            else:
                newsteps = copy.deepcopy(steps)
                newsteps.append(
                    {
                        "operation": "subspace",
                        "axes": f"wght={wght}",
                        "other_args": "--update-name-table"
                    }
                )
                newsteps.append({"postprocess": "fix", "fixargs": "--include-source-fixes"})
                config["recipe"][output] = newsteps

with open("sources/config.yaml", "w") as file:
    yaml.dump(config, file, sort_keys=False, default_flow_style = False)
