import sys
from fontTools.ttLib import TTFont


def main():
    fpath = sys.argv[1]
    font = TTFont(fpath)

    font["post"].italicAngle = 0
    font.save(fpath)


if __name__ == "__main__":
    main()
