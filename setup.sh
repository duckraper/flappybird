#!/usr/bin/env bash

if ! command -v pyinstaller &> /dev/null
then
    echo "PyInstaller could not be found"
    echo "Installing PyInstaller..."
    pip install pyinstaller
fi

pyinstaller --noconfirm --log-level=WARN \
    --nowindow \
    --add-data="README.md:." \
    --add-data "assets:assets" \
    --add-data "data:data" \
    --icon=assets/img.ico \
    --name=flappybird \
    ./src/main.py
