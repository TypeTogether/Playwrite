# Construct a builder config file from the data in data/models-all.csv
import csv
import yaml
import copy

config = {
    "sources": ["Playwrite_MM.glyphspackage"],
    "recipe": {
        "../fonts/variable/Playwrite_MM[SPED,YEXT,slnt,wght].ttf": [
            {"source": "Playwrite_MM.glyphspackage"},
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
        return name + "Italic"


UC_ORDER = (
    "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z "
    "U+00C6 U+00D0 U+0132 U+014a U+0152 U+00DE U+1E9E".split()
)

LC_ORDER = (
    "a b c d e f g h i j k l m n o p q r s t u v w x y z "
    "U+00E6 U+00F0 U+0133 U+014B U+0153 U+00FE U+00DF U+0131 U+0237".split()
)


class Model:
    source_file = "Playwrite_MM.glyphspackage"
    guidelines_source = "Playwrite-Guidelines.glyphs"
    family_name = "Playwrite"

    def __init__(self, model_dict):
        self.model_dict = model_dict

    @property
    def mapping(self):
        new_ucs = self.model_dict["UC"].split(" ")
        new_lcs = self.model_dict["lc"].split(" ")

        mapping = {}
        for old, new in zip(UC_ORDER, new_ucs):
            mapping[old] = new
        for old, new in zip(LC_ORDER, new_lcs):
            mapping[old] = new

        return mapping

    @property
    def name(self):
        model_name = self.model_dict["Country"]
        if "_" in self.model_dict["lang_tag"]:
            model_name += " " + self.model_dict["lang_tag"].split("_")[1]
        return model_name

    @property
    def file_name(self):
        return self.name.replace(" ", "")

    @property
    def axes(self):
        if "-" in self.model_dict["slnt"]:
            return "slnt,wght"
        return "wght"

    @property
    def instancer_params(self):
        return " ".join(
            [
                f"YEXT={self.model_dict['YEXT']}",
                f"SPED={self.model_dict['SPED']}",
                f"slnt={self.model_dict['slnt'].replace('-',':')}",
            ]
        )

    @property
    def variable_postprocess_steps(self):
        return [
            {"operation": "subspace", "axes": self.instancer_params},
            {"operation": "remap", "args": "--deep", "mappings": self.mapping},
            {"operation": "hbsubset"},
            {"operation": "fix", "fixargs": "--include-source-fixes" },
            {"operation": "buildStat", "other_args": "--src " + self.stat_file},
        ]

    @property
    def variable_steps(self):
        return (
            [
                {"source": self.source_file},
                {
                    "operation": "buildVariable",
                    "fontmake_args": (
                        "--no-production-names --filter ... "
                        "--filter FlattenComponentsFilter "
                        "--filter DecomposeTransformedComponentsFilter"
                    ),
                },
            ]
            + self.variable_postprocess_steps
            + [
                {"operation": "rename", "name": f"{self.family_name} {self.name}"},
            ]
        )

    @property
    def guideline_steps(self):
        return (
            [
                {"source": self.source_file},
                {
                    "operation": "exec",
                    "exe": "python3 ../scripts/add-guidelines.py",
                    "args": f"-o {self.guidelines_source} --overlap 200 {self.source_file}",
                },
                {"source": self.guidelines_source},
                {
                    "operation": "buildVariable",
                    "fontmake_args": (
                        "--no-production-names --filter ... "
                        "--filter FlattenComponentsFilter "
                        "--filter DecomposeTransformedComponentsFilter"
                    ),
                },
            ]
            + self.variable_postprocess_steps
            + [
                {
                    "operation": "rename",
                    "name": f"{self.family_name} {self.name} Guidelines",
                },
            ]
        )

    @property
    def variable_filename(self):
        return f"../fonts/variable/{self.family_name}{self.file_name}[{self.axes}].ttf"

    @property
    def guideline_filename(self):
        return f"../fonts/variable/{self.family_name}{self.file_name}-Guidelines[{self.axes}].ttf"

    @property
    def stat_file(self):
        if "-" in self.model_dict["slnt"]:
            return "stat-italic.yaml"
        return "stat.yaml"

    def static_filename(self, style, italic=False):
        if italic:
            return f"../fonts/static/{self.file_name}/{self.family_name}{self.file_name}-{to_italic(style)}.ttf"
        return f"../fonts/static/{self.file_name}/{self.family_name}{self.file_name}-{style}.ttf"

    def static_steps(self, style, italic=False):
        wght = STATICS[style]
        subspace_axes = f"wght={wght}"
        if italic:
            if "-" not in self.model_dict["slnt"]:
                return
            low, high = [int(x) for x in self.model_dict["slnt"].split("-")]
            subspace_axes += f" slnt={low}"
        return self.variable_steps + [
            {
                "operation": "subspace",
                "axes": subspace_axes,
                "other_args": "--update-name-table",
            },
            {"postprocess": "fix", "fixargs": "--include-source-fixes"},
        ]


with open("sources/data/models-all.csv", "r") as file:
    reader = csv.DictReader(file, delimiter=";")
    for ix, model in enumerate(reader):
        model = Model(model)
        config["recipe"][model.variable_filename] = model.variable_steps
        config["recipe"][model.guideline_filename] = model.guideline_steps

        # # And now for statics
        for style in STATICS.keys():
            upright_filename = model.static_filename(style, italic=False)
            config["recipe"][upright_filename] = model.static_steps(style, italic=False)

            italic_steps = model.static_steps(style, italic=True)
            if italic_steps:
                italic_filename = model.static_filename(style, italic=True)
                config["recipe"][italic_filename] = model.static_steps(
                    style, italic=True
                )

with open("sources/config.yaml", "w") as file:
    yaml.dump(config, file, sort_keys=False, default_flow_style=False)
