import os
import re
import json

used_names = set()

def has_image_file(folder_path):
    # Check if the folder contains a .png or .jpg file
    for file in os.listdir(folder_path):
        if file.lower().endswith(('.png', '.jpg')):
            return True
    return False

def process_folder(folder_path):
    # Extract information from folder name
    folder_name = os.path.basename(folder_path)

    # Check if the folder name has more than 2 underscores and contains an image file
    if folder_name.count('_') < 2 or not has_image_file(folder_path):
        return 0

    parts = folder_name.split('_')
    product_code = parts[1]
    asset_code = parts[2]
    raw_name = '_'.join(re.findall('[A-Z][a-z0-9]*', parts[-1]))

    # Check if the name has been used before
    name = raw_name
    count = 2
    while name in used_names:
        name = f"{raw_name}_{count}"
        count += 1

    used_names.add(name)

    # Create dictionary
    material_dict = {
        "version": 1,
        "type": "material",
        "productCode": product_code,
        "assetcode": asset_code,
        "name": name.replace('_', ' '),  # Replace underscores with spaces
        "tags": "",
        "res": ""
    }

    # Write dictionary to .gsgm file using folder name
    output_file_path = os.path.join(folder_path, f"{folder_name}.gsgm")
    with open(output_file_path, 'w') as file:
        json.dump(material_dict, file, indent=2)

    return 1  # Return 1 for counting a successful file creation

def process_directory(directory_path):
    gsgm_count = 0  # Counter for gsgm files

    # Get list of subdirectories
    subdirectories = [d for d in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, d))]

    # Process each subdirectory
    for subdirectory in subdirectories:
        subdirectory_path = os.path.join(directory_path, subdirectory)
        gsgm_count += process_folder(subdirectory_path)

        # Recursively process subdirectories
        gsgm_count += process_directory(subdirectory_path)

    # Delete .gsgm files without characters before the suffix
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".gsgm") and len(file.split('.')[0]) == 0:
                os.remove(os.path.join(root, file))

    print(f"{gsgm_count} .gsgm files created in {os.path.basename(directory_path)}")
    return gsgm_count

# Prompt user for directories
while True:
    directory_input = input("Enter directory path or (x) to exit: ")
    if directory_input.lower() == 'x':
        break

    if os.path.isdir(directory_input):
        process_directory(directory_input)
    else:
        print("Invalid directory path. Please try again.")
