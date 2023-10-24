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
        "../sources-ufo/designspace-models/_Playwrite-SOURCES.designspace")
    slant = val["slnt"]
    extend = val["YEXT"]
    speed = val["SPED"]
    # if slant range (hasItalic)
    if type(slant) is str:
        hasItalic = True
        it_slant = int(slant.split("-")[-1])
        slant = int(slant.split("-")[0])
    else:
        hasItalic = False

    # make weight instances
    for w_value in weightStyles.keys():
        mFamilyName = f"Playwrite {mTag.replace('_', ' ')}"
        iStyleName = weightStyles[w_value]  # (from weight style-value)
        family_no_space = mFamilyName.replace(" ", "")
        iPostscriptFontName = f"{family_no_space}-{iStyleName}"
        # make instance
        i = InstanceDescriptor()
        i.familyName = mFamilyName
        i.styleName = iStyleName
        i.name = f"{mFamilyName} {iStyleName}"
        # i.designLocation = dict(Weight=w_value, Slant=slant,
        #                         Extenders=extend, Speed=speed)
        i.designLocation = {"Weight": w_value,
                            "Slant": slant,
                            "Vertical Extensions": extend,
                            "Speed": speed
                            }
        i.postScriptFontName = iPostscriptFontName
        if iStyleName != "Regular":
            i.styleMapFamilyName = f"{mFamilyName} {iStyleName}"
        else:
            i.styleMapFamilyName = f"{mFamilyName}"
        i.styleMapStyleName = "regular"
        i.path = f"../sources-ufo/instance_ufo/{iPostscriptFontName}.ufo"
        doc.addInstance(i)
        # if italic
        if hasItalic is True:
            # italic values
            mFamilyName = f"Playwrite {mTag.replace('_', ' ')}"
            family_no_space = mFamilyName.replace(" ", "")
            if iStyleName != "Regular":
                it_iStyleName = iStyleName + " Italic"
                it_iPostscriptFontName = f"{family_no_space}-{iStyleName}Italic"
            else:
                it_iStyleName = "Italic"
                it_iPostscriptFontName = f"{family_no_space}-Italic"
            # make instance
            it = InstanceDescriptor()
            it.familyName = mFamilyName
            it.styleName = it_iStyleName
            it.name = f"{mFamilyName} {it.styleName}"
            # it.designLocation = dict(Weight=w_value, Slant=it_slant,
            #                          Extenders=extend, Speed=speed)
            it.designLocation = {"Weight": w_value,
                                 "Slant": it_slant,
                                 "Vertical Extensions": extend,
                                 "Speed": speed
                                 }
            it.postScriptFontName = it_iPostscriptFontName
            if iStyleName != "Italic":
                it.styleMapFamilyName = f"{mFamilyName} {iStyleName}"
            else:
                it.styleMapFamilyName = f"{mFamilyName}"
            it.styleMapStyleName = "italic"
            it.path = f"../sources-ufo/instance_ufo/{it_iPostscriptFontName}.ufo"
            doc.addInstance(it)

    # Write model.designspace
    outputPath = f"../sources-ufo/designspace-models/{mTag}.designspace"
    doc.write(outputPath)
    print(f"Written {mTag}.designspace")

print("\nWritten all designspaces for all languages")
