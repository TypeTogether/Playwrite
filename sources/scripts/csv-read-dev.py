# read csv


class langModel(object):
    """docstring for langModel"""

    def __init__(self, csv_line):
        super(langModel, self).__init__()
        self.csv_line = csv_line
        csv_values = csv_line.split(";")
        self.country = csv_values[0]
        self.lang_tag = csv_values[1]
        self.slnt = csv_values[2]
        self.extd = csv_values[3]
        self.sped = csv_values[4]
        self.UC_class = csv_values[5]
        self.lc_class = csv_values[6]
        #
        self.UC_text = self.makeUCClassString(self.UC_class)
        self.lc_text = self.makelcClassString(self.lc_class)

    def makeUCClassString(self, string):
        return f"@UC_{self.lang_tag} = [{string}];"

    def makelcClassString(self, string):
        return f"@lc_{self.lang_tag} = [{string}];"


with open('../data/models-all.csv', "r") as csv:
    lines = csv.readlines()
    for l in lines:
        lang_mod = langModel(l)
        print(lang_mod.lc_text)
