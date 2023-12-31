# Convert-GSG-materials

## Overview
This Python script automates the creation of `.gsgm` data files for GSG materials so that they can be detected and imported by GSG's Houdini and Blender importer addons. It recursively processes directories and their subdirectories, using information from folder names to generate `.gsgm` files.

## Usage
1. Follow the prompt:
   - Enter the directory path to the materials.
   - Input `(x)` to exit the prompt loop.
2. The script will generate `.gsgm` data files for the materials.

### Notes
- `.gsgm` files will be created based on the material's folder name information. Examples: `GSG_MC028_A001_Fabric` , `Blob_Marble`.
- Existing `.gsgm` files in the specified directories will have their contents overwritten and updated.

## Example
Suppose we have a folder with all our materials that has a structure like this located at "E:\GSG_March2023_Update\materials":

![image](https://cdn.discordapp.com/attachments/734616060611002379/1178109715750862858/image.png?ex=6574f32c&is=65627e2c&hm=15ec3c21d7ea1dbe4cc61c4d8f026d70fe40fb08857f70ab84972eeaf11b0f1b&)

Each folder has 10-70 subfolders of materials. Instead of entering each folder individually, you can enter the main folder that encompasses all of them which will be recursively searched. In this case "E:\GSG_March2023_Update\materials" from the example above will give the following output and generate `.gsgm` files for all 272 materials: 

![image](https://cdn.discordapp.com/attachments/734616060611002379/1178127424769241158/image.png?ex=657503aa&is=65628eaa&hm=082f76d2b45e495561b95e1e843dde5fdcdc63762e997aab3d889e6db1365b4b&)

Example of the materials being imported and detected by GSG's Houdini material importer:

![image](https://cdn.discordapp.com/attachments/734616060611002379/1178440456024105000/image.png?ex=65762733&is=6563b233&hm=9d11c4edefefa4792fddae1d04f1d4434d5676930566c612b24e6115bced364d&)
