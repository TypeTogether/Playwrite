#!/bin/sh
FONT=$1
if [ -z "$FONT" ]; then
  echo "Usage: $0 fonts/variable/PlaywriteWhatever.ttf"
  exit 1
fi

make venv
. venv/bin/activate
python3 scripts/create-builder-config.py
gftools-builder --no-ninja sources/config.yaml
cd sources
ninja ../$FONT

