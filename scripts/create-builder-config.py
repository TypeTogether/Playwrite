# Construct a builder config file from the data in data/models-all.csv
import csv
from dataclasses import dataclass
import yaml

UC_ORDER = (
    "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z "
    "U+00C6 U+00D0 U+0132 U+014a U+0152 U+00DE U+1E9E".split()
)

LC_ORDER = (
    "a b c d e f g h i j k l m n o p q r s t u v w x y z "
    "U+00E6 U+00F0 U+0133 U+014B U+0153 U+00FE U+00DF U+0131 U+0237".split()
)

FG_ORDER = (
    "U+0030 U+0031 U+0032 U+0033 U+0034 U+0035 U+0036 U+0037 U+0038 U+0039".split()
)

locl_required = {
    "CZ": "CSY",
    "ES": "ESP",
    "NL": "NLD",
    "RO": "ROM",
    "SK": "SKY",
}

added_values = set([0, -18])
slant_values = [
    {"name": "Regular", "value": 0},
    {"name": "Italic", "value": -18},
]

config = {
    "sources": ["Playwrite_MM.glyphspackage"],
    "doGuidelines": False,
    "buildStatic": True,
    "buildColorVariable": False,
    "recipeProvider": "fontprimer",
    "variants": [],
    "recipe": {},
    "stat": [
        {
            "name": "Weight",
            "tag": "wght",
            "values": [
                {"name": "Thin", "value": 100},
                {"name": "ExtraLight", "value": 200},
                {"name": "Light", "value": 300},
                {"name": "Regular", "value": 400, "flags": 2},
            ],
        },
        {
            "name": "Slant",
            "tag": "slnt",
            "values": slant_values,
        },
        {"name": "Speed", "tag": "SPED"},
        {"name": "Y Extension", "tag": "YEXT"},
    ],
}


@dataclass
class Model:
    _Country: str
    _lang_tag: str
    _slnt: str
    _YEXT: int
    _SPED: int
    _UC: str
    _lc: str
    _fg: str

    mapping: dict = None

    def __post_init__(self):
        new_ucs = self._UC.strip().split()
        new_lcs = self._lc.strip().split()
        new_figs = self._fg.strip().split()
        self.mapping = {}
        for old, new in zip(UC_ORDER, new_ucs):
            self.mapping[old] = new
        for old, new in zip(LC_ORDER, new_lcs):
            self.mapping[old] = new
        for old, new in zip(FG_ORDER, new_figs):
            self.mapping[old] = new
    @property
    def name(self):
        return self._lang_tag.replace("_", " ")

    @property
    def remap_layout(self):
        if self._lang_tag in locl_required:
            return [
                {
                    "operation": "remapLayout",
                    "args": "'latn/"
                    + locl_required[self._lang_tag]
                    + "/locl => latn/dflt/locl'",
                }
            ]
        return []

    @property
    def remap_glyphs(self):
        return {
            "operation": "remap",
            "args": "--deep",
            "mappings": dict(self.mapping),
        }

    @property
    def has_italic(self):
        return "-" in self._slnt

    def slnt_value(self, italic=False):
        if self.has_italic:
            reg_value, ital_value = self._slnt.split("-")
            if italic:
                val = ital_value
            else:
                val = reg_value
        else:
            if italic:
                raise ValueError("Variant has no italic")
            val = self._slnt
        val = int(val)
        return val

    @property
    def alias(self):
        return self._lang_tag.replace("_", " ")

    def subspace(self, italic=False, drop_weight=False):
        op = {
            "operation": "subspace",
            "axes": f"YEXT={self._YEXT} SPED={self._SPED} slnt=-{self.slnt_value(italic)}",
        }
        if drop_weight:
            op["axes"] += " wght=200"
        if italic:
            op["args"] = "--update-name-table"
        return op

    @property
    def adobe_fix(self):
        return {
            "operation": "remapLayout",
            "args": "'locl=>|calt' 'ccmp=>|calt'",
        }

    def basic_config(self, italic=False):
        conf = {"name": self.name, "alias": self.alias}
        if italic:
            conf["italic"] = True
        conf["steps"] = model.remap_layout + [
            self.subspace(italic=italic),
            self.remap_glyphs,
            self.adobe_fix,
            {"operation": "hbsubset", "args": "--passthrough-tables"},
        ]
        return conf

    def add_used_slants_to_stat(self):
        used_slnts = [self.slnt_value(italic=False)]
        if self.has_italic:
            used_slnts.append(self.slnt_value(italic=True))
        for used_slnt in used_slnts:
            if -used_slnt not in added_values:
                added_values.add(-used_slnt)
                slant_values.append(
                    {"name": "Italic", "value": -used_slnt},
                )

    def guidelines_recipe(self, italic=False):
        ops = [
            {"source": "generated/Playwrite-Guides.glyphs"},
            {
                "args": "--filter ...  --filter FlattenComponentsFilter --filter DecomposeTransformedComponentsFilter --no-production-names",
                "operation": "buildVariable",
            },
            {"operation": "fix"},
        ]
        if italic:
            ops.append(
                {
                    "operation": "buildStat",
                    "args": "--src generated/guidelines-stat.yaml",
                }
            )
        ops += [
            model.subspace(italic=italic, drop_weight=True),
            model.remap_glyphs,
            model.adobe_fix,
            {"operation": "hbsubset", "args": "--drop-tables=STAT"},
            {"operation": "fix", "args": "--include-source-fixes"},
        ]
        if not italic:
            ops.append(
                {
                    "operation": "exec",
                    "exe": "gftools-fontsetter",
                    "args": "-o $out $in zero-post.yaml",
                }
            )
        ops.append(
            {
                "operation": "rename",
                "args": "--just-family",
                "name": "Playwrite " + model.alias + " Guides",
            },
        )
        return ops


with open("sources/data/models-all.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=";")
    for ix, model in enumerate(reader):
        model = Model(**{"_" + k: v for k, v in model.items()})
        if model.has_italic:
            # Regular is easy
            regular = model.basic_config(italic=False)
            regular["steps"] += [
                # Fix first is correct here. I know it's different to the others.
                {"operation": "fix", "args": "--include-source-fixes"},
                {"operation": "buildStat", "args": "--src stat.yaml"},
            ]
            config["variants"].append(regular)

            # Add an explicit recipe for guidelines
            config["recipe"][
                "../fonts/ttf/Playwrite"
                + model.alias.replace(" ", "")
                + "Guides-Regular.ttf"
            ] = model.guidelines_recipe(italic=False)

            italic = model.basic_config(italic=True)
            italic["steps"] += [
                {"operation": "buildStat", "args": "--src stat-italic.yaml"},
                {"operation": "fix", "args": "--include-source-fixes"},
            ]
            config["variants"].append(italic)
            config["recipe"][
                "../fonts/ttf/Playwrite"
                + model.alias.replace(" ", "")
                + "Guides-Italic.ttf"
            ] = model.guidelines_recipe(italic=True)

        else:
            regular = model.basic_config(italic=False)
            regular["steps"].extend(
                [
                    {
                        "operation": "buildStat",
                        "args": "--src stat-standalone.yaml",
                    },
                    {"operation": "fix", "args": "--include-source-fixes"},
                    {
                        "operation": "exec",
                        "exe": "gftools-fontsetter",
                        "args": "-o $out $in zero-post.yaml",
                    },
                ],
            )

            config["variants"].append(regular)

            # Add an explicit recipe for guidelines
            config["recipe"][
                "../fonts/ttf/Playwrite"
                + model.alias.replace(" ", "")
                + "Guides-Regular.ttf"
            ] = model.guidelines_recipe(italic=False)

        model.add_used_slants_to_stat()

with open("sources/config.yaml", "w") as file:
    yaml.dump(config, file, sort_keys=False, default_flow_style=False)

with open("sources/generated/omni-stat.yaml", "w") as file:
    yaml.dump(config["stat"], file, sort_keys=False, default_flow_style=False)

# Rename ExtraLight to Regular in guidelines
config["stat"][0]["values"][1]["name"] = "Regular"
with open("sources/generated/guidelines-stat.yaml", "w") as file:
    yaml.dump(config["stat"], file, sort_keys=False, default_flow_style=False)
