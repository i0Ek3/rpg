#!/bin/bash

# Pack the browser plugin into a zip file
echo "Packaging RPG Browser Plugin..."

PLUGIN_DIR="plugin"
BUILD_DIR="dist"
VERSION=$(grep '"version"' $PLUGIN_DIR/manifest.json | cut -d '"' -f 4)
OUT_FILE="${BUILD_DIR}/rpg-plugin-v${VERSION}.zip"

mkdir -p $BUILD_DIR

# Clean up any existing zip
rm -f $OUT_FILE

# Zip the plugin directory contents
cd $PLUGIN_DIR
zip -r "../$OUT_FILE" . -x "*.DS_Store*"

echo "Successfully packaged to $OUT_FILE"
echo "To install in Chrome/Edge:"
echo "1. Go to chrome://extensions"
echo "2. Enable 'Developer mode'"
echo "3. Click 'Load unpacked' and select the '$(pwd)' directory"
echo "To distribute as CRX:"
echo "1. Use 'Pack extension' button in chrome://extensions and select the same directory."
