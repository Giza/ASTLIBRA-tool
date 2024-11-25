# ASTLIBRA-tool
Program for changing game files ASTLIBRA (.dxa .dig LOCALIZE_.DAT)

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
