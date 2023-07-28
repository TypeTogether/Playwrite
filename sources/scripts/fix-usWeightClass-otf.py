# Check if any otfs and ttfs have usWeightClass values of 100 and 200
# and changes them to 250 and 275 consecutively.
# Files are overwritten.
# Based on Ben Kiel's setUseTypoMetricsFalse script:
# https://github.com/Typefounding/setUseTypoMetricsFalse

import sys
import os
from fontTools.ttLib import TTFont


def fixusWeightClass(fontPath):
    # Get Font object from path
    font = TTFont(fontPath)
    # Get the OS/2 Table
    os2 = font["OS/2"]
    # Get the WeightClass
    wght = os2.usWeightClass

    # Check if Thin
    if wght == 100:
        # Set to 250
        os2.usWeightClass = 250
        print(f"{os.path.basename(fontPath)} usWeightClass {str(wght)} → {str(os2.usWeightClass)}")
        # Save font
        font.save(fontPath)
        font.close()
    # Check if UltraLight
    elif wght == 200:
        # Set to 275
        os2.usWeightClass = 275
        print(f"{os.path.basename(fontPath)} usWeightClass {str(wght)} → {str(os2.usWeightClass)}")
        # Save font
        font.save(fontPath)
        font.close()
    else:
        print(fontPath + " Nothing to fix.")


def main():
    fpath = sys.argv[1]
    fixusWeightClass(fpath)


if __name__ == "__main__":
    main()
