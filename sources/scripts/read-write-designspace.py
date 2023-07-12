from fontTools.designspaceLib import (DesignSpaceDocument, AxisDescriptor,
                                      SourceDescriptor, InstanceDescriptor)
doc = DesignSpaceDocument.fromfile(
    "../sources-ufo/designspace-models/Playpen-SOURCES.designspace")

# print(doc.formatVersion)
# print(doc.elidedFallbackName)
# print(doc.axes)
# print(doc.axisMappings)
# print(doc.locationLabels)
# print(doc.rules)
# print(doc.rulesProcessingLast)
# print(doc.sources)
# print(doc.variableFonts)
# print(doc.instances)
# print(doc.lib)

# <instance name="Playpen COL Light" familyname="Playpen COL" stylename="Light" filename="../instance_ufo/PlaypenCOL-Light.ufo" postscriptfontname="PlaypenCOL-Light" stylemapfamilyname="Playpen COL Light" stylemapstylename="regular">
#   <location>
#     <dimension name="Weight" uservalue="300"/>
#     <dimension name="Slant" xvalue="18"/>
#     <dimension name="Extenders" xvalue="416"/>
#     <dimension name="Speed" xvalue="50"/>
#   </location>
# </instance>

# -------------------------
# variables
mTag = "COL"
mFamilyName = f"Playpen {mTag}"
# weight styles dict {"Thin": 100, "ExtraLight": 200, "Light": 300,
# "Regular": 400}
iStyleName = "Light"  # (from weight style-value)
iWeight = "Light"
f = mFamilyName.replace(" ", "")
iPostscriptFontName = f"{f}-{iStyleName}"
# values will come from csv
weight = 300
slant = 18
extend = 416
speed = 50

# make instance
i = InstanceDescriptor()
i.familyName = mFamilyName
i.styleName = iStyleName
i.name = f"{mFamilyName} {iStyleName}"
i.designLocation = dict(Weight=weight, Slant=slant,
                        Extenders=extend, Speed=speed)
i.postScriptFontName = iPostscriptFontName
# unless Regular (should be removed)
i.styleMapFamilyName = f"{mFamilyName} {iStyleName}"
i.styleMapStyleName = "regular"
i.path = f"../instance_ufo/{iPostscriptFontName}.ufo"
# i.lib['com.coolDesignspaceApp.specimenText'] = 'Hamburgerwhatever'
doc.addInstance(i)

outputPath = "../sources-ufo/designspace-models/myprototype.designspace"
doc.write(outputPath)
