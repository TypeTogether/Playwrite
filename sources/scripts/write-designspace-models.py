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

# models data
for mTag, val in modelsDataDict.items():
    # designspace with the sources
    doc = DesignSpaceDocument.fromfile(
    "../sources-ufo/designspace-models/_Playpen-SOURCES.designspace")
    slant = val["slnt"]
    extend = val["EXTD"]
    speed = val["SPED"]
    # if slant range (hasItalic)
    if type(slant) is str:
        hasItalic = True
        # take first value (0) by now
        slant = int(slant.strip("-")[0])
    else:
        hasItalic = False

    # make weight instances
    for w_value in weightStyles.keys():
        mFamilyName = f"Playpen {mTag.replace('_', ' ')}"
        iStyleName = weightStyles[w_value]  # (from weight style-value)
        family_no_space = mFamilyName.replace(" ", "")
        iPostscriptFontName = f"{family_no_space}-{iStyleName}"
        # make instance
        i = InstanceDescriptor()
        i.familyName = mFamilyName
        i.styleName = iStyleName
        i.name = f"{mFamilyName} {iStyleName}"
        i.designLocation = dict(Weight=w_value, Slant=slant,
                                Extenders=extend, Speed=speed)
        i.postScriptFontName = iPostscriptFontName
        if iStyleName != "Regular":
            i.styleMapFamilyName = f"{mFamilyName} {iStyleName}"
        else:
            i.styleMapFamilyName = f"{mFamilyName}"
        i.styleMapStyleName = "regular"
        i.path = f"../sources-ufo/instance_ufo/{iPostscriptFontName}.ufo"
        doc.addInstance(i)

    outputPath = f"../sources-ufo/designspace-models/{mTag}.designspace"
    doc.write(outputPath)
    print(f"Written {mTag}.designspace")

print("Written all designspaces for all languages")
