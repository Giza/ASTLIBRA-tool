# ASTLIBRA-tool
Program for changing game files ASTLIBRA (.dxa, .dig, LOCALIZE_.DAT, .dft)

# Extract .dxa
To extract archives, drag the archive to ASTLIBRA_Dec.exe

example:
```
ASTLIBRA_Dec.exe Image2K.dxa
```

After extraction, the archive file can be deleted so the game reads files from the folder.

# Conver .dig to .png
Copy script to .dig files folder

Start script
```
python _DIMG.py
```
The colors will have to be inverted manually. Or someone will write the correct converter=)

# Conver .png to .dig
The game can read PNG files directly, so just rename the PNG file extension to DIG.

# Extract\Import LOCALIZE_.DAT
Before extraction, the file needs to be decoded. You can extract it from the game dump or use a pre-prepared file.

Extract:
```
python _ALOC.py LOCALIZE_.DAT_dec _extracted_texts.csv -e
```
Import:
```
python _ALOC.py LOCALIZE_.DAT_dec _extracted_texts.csv -p
```

To ensure the text is in order, sort by the Offset_start column in ascending order, and then, before packaging, sort by the I column.

To allow the game to see the packed text after unpacking, the .exe file needs to be slightly modified. Specifically, the byte sequence
```
89 41 F8 8B 41 FC C1 C8 04 89 41 FC
```
to
```
90 90 90 8B 41 FC C1 C8 04 90 90 90
```
This will disable the attempt to decode the localization file.

# Create FONT
example:
```
CreateDXFontData.exe /F"Arial Black" /B4 /S12 /A_test.txt /O"FONT_SEZANU_S12.dft"
```
