if ! command -v pyinstaller &> /dev/null
then
    echo "PyInstaller could not be found"
    echo "Installing PyInstaller..."
    pip install pyinstaller
fi

pyinstaller --noconfirm --log-level=WARN \
    --onefile --nowindow \
    --add-data="README.md:." \
    --add-data "assets:assets" \
    --icon=assets/img.ico \
    --name=flappybird \
    main.py
