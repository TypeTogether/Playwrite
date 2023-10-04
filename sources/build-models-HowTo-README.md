# How to Build font models

## Build instructions

**Playwrite** fonts are built using [fontParts](https://github.com/robotools/fontParts), [gftools](https://github.com/googlefonts/gftools) and [glyphspkg](https://github.com/jenskutilek/glyphspkg).

### Clone the repository and create a virtual environment

In order to build the fonts you will need to follow these steps:

```sh
# Move to the folder you want the repository in:
cd your/repositories/folder
# Clone the repository:
git clone https://github.com/TypeTogether/Playwrite.git
# Move to the repository folder:
cd your/repositories/folder/Playwrite
# Create a virtual environment:
python3 -m venv env
# Activate your virtual environment
source env/bin/activate
# Upgrade pip before installing packages:
pip install --upgrade pip
# Install the needed Python packages:
pip install -r requirements.txt
```

Now you should be ready for building the fonts.

### Build model fonts

Each model has a tag as *COUNTRY(_MODEL)*. You can check the list of tags in `sources/data/model-tags-list.txt`.

#### Building model static ttf fonts:

```sh
cd sources/sources-ufo
sh build-models-static.sh TAG
# You can provide several tags separated by a space for building more than just one:
sh build-models-static.sh TAG1 TAG2 […]
# You can build all models passing the "ALL" parameter:
sh build-models-static.sh ALL
# (This will take a while...)
```

If all goes well, built model fonts will show up in `Playwrite/fonts-models/fonts-TAG/static/ttf`

As a real code example:

```sh
sh build-models-static.sh ARG
# or
sh build-models-static.sh ARG AUS_NSW COL CZE
```

#### Variable model font (weight) `wght` axis

```sh
cd sources/sources-ufo
sh build-models-var.sh TAG
# (same applies for several tags and ALL as in statics build)
```

Built variable model (`wght` axis only) should be in: `Playwrite/fonts-models/fonts-TAG/variable/PlaywriteTAG[wght].ttf`

## Source file

**Playwrite** source file is in Glyphs `.glyphspackage` format.

### Version 1.000
First release of Playwrite.

## License

Licensed under the [SIL Open Font License (v1.1)](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL)
