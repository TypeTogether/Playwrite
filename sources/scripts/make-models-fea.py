# Make specific features for all models from the csv database


UC_src = "@UC_src = [A B C D E F G H I J K L M N O P Q R S T U V W X Y Z];"
lc_src = "@lc_src = [a b c d e f g h i j k l m n o p q r s t u v w x y z];"


class langModel(object):
    """docstring for langModel"""

    def __init__(self, csv_line):
        super(langModel, self).__init__()
        self.csv_line = csv_line
        csv_values = csv_line.split(";")
        # self.country = csv_values[0]
        self.lang_tag = csv_values[1]
        # self.slnt = csv_values[2]
        # self.extd = csv_values[3]
        # self.sped = csv_values[4]
        self.UC_class = csv_values[5]
        self.lc_class = csv_values[6]
        #
        self.UC_text = self.makeUCClassString(self.UC_class)
        self.lc_text = self.makelcClassString(self.lc_class)
        #
        self.fea_code = [f"# {self.lang_tag}", UC_src, lc_src, self.UC_text, self.lc_text]

    def makeUCClassString(self, string):
        return f"@UC_{self.lang_tag} = [{string}];"

    def makelcClassString(self, string):
        return f"@lc_{self.lang_tag} = [{string}];"

    def makeFeaText(self):
        self.fea_code.append(f"\nsub [@UC_src @lc_src] by [@UC_{self.lang_tag} @lc_{self.lang_tag}];")
        return "\n".join(self.fea_code)

    def writeFeaFile(self, folder):
        with open(f"{folder}{self.lang_tag}.fea", "w") as fea:
            featext = self.makeFeaText()
            fea.write(featext)
            fea.close()


with open("../data/models-all.csv", "r") as csv:
    lines = csv.readlines()
    models_fea_folder = "../features/fea-models/"
    for l in lines:
        lang_mod = langModel(l)
        lang_mod.writeFeaFile(models_fea_folder)

print(" ✅ Done writing models feature")
