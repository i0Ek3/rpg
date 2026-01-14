#!/bin/bash

# Pack the browser plugin into zip and crx files
echo "Packaging RPG Browser Plugin..."

PLUGIN_DIR="plugin"
DIST_DIR="dist"
VERSION=$(grep '"version"' $PLUGIN_DIR/manifest.json | cut -d '"' -f 4)
ZIP_FILE="${DIST_DIR}/rpg-plugin-v${VERSION}.zip"
CRX_FILE="${DIST_DIR}/rpg-plugin-v${VERSION}.crx"
PEM_FILE="rpg-plugin.pem"

mkdir -p $DIST_DIR

# 1. Create ZIP package
echo "Creating ZIP package..."
rm -f $ZIP_FILE
cd $PLUGIN_DIR
zip -r "../$ZIP_FILE" . -x "*.DS_Store*" -x "__MACOSX*"
cd ..

# 2. Create CRX package
CHROME_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [ -f "$CHROME_PATH" ]; then
    echo "Creating CRX package using Google Chrome..."
    
    # Check if PEM exists, if not Chrome will generate one
    if [ -f "$PEM_FILE" ]; then
        "$CHROME_PATH" --pack-extension="$(pwd)/$PLUGIN_DIR" --pack-extension-key="$(pwd)/$PEM_FILE" --no-message-box
    else
        "$CHROME_PATH" --pack-extension="$(pwd)/$PLUGIN_DIR" --no-message-box
        # Chrome creates plugin.crx and plugin.pem next to the plugin folder
        # Move them to our desired locations
        mv "${PLUGIN_DIR}.pem" "$PEM_FILE"
    fi
    
    # Move the generated crx to dist
    mv "${PLUGIN_DIR}.crx" "$CRX_FILE"
    
    echo "Successfully packaged to $CRX_FILE"
    echo "Private key saved to $PEM_FILE (Keep this safe for future updates!)"
else
    echo "Google Chrome not found at $CHROME_PATH, skipping CRX generation."
fi

echo "All packages generated in $DIST_DIR/"
echo "To install the CRX:"
echo "1. Open Chrome/Edge extensions page (chrome://extensions)"
echo "2. Drag and drop the .crx file onto the page."
