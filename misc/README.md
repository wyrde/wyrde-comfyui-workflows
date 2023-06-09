# misc files that don't fit elsewhere


## .Exiftool_config
a configuration file that adds some SD-related tags allowing exiftool to edit them. It can read the tags but cannot edit them until they are defined.
### related:
* https://exiftool.org/
* https://github.com/hvdwolf/jExifToolGUI/releases
* https://hvdwolf.github.io/jExifToolGUI/manual/index.html#userdefinedmetadatacombinations

## workping.py
A CLI script for adding a workflow to a PNG file. Requres Pillow module (PIL). It updates the image file, make a backup if you want extra safety.
```
    /path/to/python workping.py --image "/path/to/image.png" --workflow "/path/to/workflow.json"
```
* note
  * both comfy and a111 use pillow, but it may not be installed globally. Use the path to comfy or a111's python or a venv if pillow isn't accessable by system python. Or install from below.

### related
* source: https://colab.research.google.com/drive/1hQMjNUdhMQ3rw1Wcm3_umvmOMeS_K4s8?usp=sharing#scrollTo=llbal5zlANoH
* PIL: https://pillow.readthedocs.io/en/stable/installation.html

[home](../../..)
