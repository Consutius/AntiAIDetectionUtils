@echo off
echo Compiling the project to a single executable with bundled resources...
pyinstaller --onefile --windowed --add-data "install.bat;." --add-data "requirements.txt;." --add-data "clean.py;." emojiClean.py
echo Compilation complete. Check the dist folder for the executable.
pause