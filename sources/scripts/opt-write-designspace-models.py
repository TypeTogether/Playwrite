from fontTools.designspaceLib import (DesignSpaceDocument, AxisDescriptor,
                                      SourceDescriptor, InstanceDescriptor)
from modelsData import modelsDataDict


# weights
weightStyles = {
    100: "Thin",
    200: "ExtraLight",
    300: "Light",
    400: "Regular",
}

# designspace with the sources
doc = DesignSpaceDocument.fromfile(
    "../sources-ufo/designspace-models/_Playpen-SOURCES.designspace")


def getAxisValues(model):
    __doc__ = """Return model values for every axis."""
    values = modelsDataDict[model]
    slant = values["slnt"]
    itslant = None
    extend = values["YEXT"]
    speed = values["SPED"]

    if type(slant) is str:
        it = int(slant.strip("-")[-1])
        slant = int(slant.strip("-")[0])

    return (slant, extend, speed, itslant)


def main():
    # models data
    for modeltag in modelsDataDict.keys():
        sl, xt, sp, it = getAxisValues(modeltag)
        print(modeltag, sl, xt, sp, it)

    #     # make weight instances
    #     for w_value in weightStyles.keys():
    #         mFamilyName = f"Playpen {mTag.replace('_', ' ')}"
    #         iStyleName = weightStyles[w_value]  # (from weight style-value)
    #         family_no_space = mFamilyName.replace(" ", "")
    #         iPostscriptFontName = f"{family_no_space}-{iStyleName}"
    #         # make instance
    #         i = InstanceDescriptor()
    #         i.familyName = mFamilyName
    #         i.styleName = iStyleName
    #         i.name = f"{mFamilyName} {iStyleName}"
    #         i.designLocation = dict(Weight=w_value, Slant=slant,
    #                                 Extenders=extend, Speed=speed)
    #         i.postScriptFontName = iPostscriptFontName
    #         if iStyleName != "Regular":
    #             i.styleMapFamilyName = f"{mFamilyName} {iStyleName}"
    #         else:
    #             i.styleMapFamilyName = f"{mFamilyName}"
    #         i.styleMapStyleName = "regular"
    #         i.path = f"../sources-ufo/instance_ufo/{iPostscriptFontName}.ufo"
    #         doc.addInstance(i)
    #         # if italic
    #         if hasItalic is True:
    #             # italic values
    #             mFamilyName = f"Playpen {mTag.replace('_', ' ')}"
    #             family_no_space = mFamilyName.replace(" ", "")
    #             if iStyleName != "Regular":
    #                 it_iStyleName = iStyleName + " Italic"
    #                 it_iPostscriptFontName = f"{family_no_space}-{iStyleName}Italic"
    #             else:
    #                 it_iStyleName = "Italic"
    #                 it_iPostscriptFontName = f"{family_no_space}-Italic"
    #             # make instance
    #             it = InstanceDescriptor()
    #             it.familyName = mFamilyName
    #             it.styleName = it_iStyleName
    #             it.name = f"{mFamilyName} {it.styleName}"
    #             it.designLocation = dict(Weight=w_value, Slant=it_slant,
    #                                     Extenders=extend, Speed=speed)
    #             it.postScriptFontName = it_iPostscriptFontName
    #             if iStyleName != "Italic":
    #                 it.styleMapFamilyName = f"{mFamilyName} {iStyleName}"
    #             else:
    #                 it.styleMapFamilyName = f"{mFamilyName}"
    #             it.styleMapStyleName = "italic"
    #             it.path = f"../sources-ufo/instance_ufo/{it_iPostscriptFontName}.ufo"
    #             doc.addInstance(it)

    #     # Write model.designspace
    #     outputPath = f"../sources-ufo/designspace-models/{mTag}.designspace"
    #     doc.write(outputPath)
    #     print(f"Written {mTag}.designspace")

    # print("Written all designspaces for all languages")


if __name__ == '__main__':
    main()
