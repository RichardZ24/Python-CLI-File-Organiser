from pathlib import Path
import argparse
import shutil

SUFFIX_DICT = {
    # Images
    ".jpeg": "Images",
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",

    # Videos
    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",

    # Audio
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".aac": "Audio",

    # Compressed
    ".zip": "Compressed",
    ".rar": "Compressed",
    ".7z": "Compressed",
    ".gz": "Compressed",
    ".tar": "Compressed",

    # Code
    ".py": "Code",
    ".c": "Code",
    ".cpp": "Code",
    ".js": "Code",
    ".html": "Code",

    # Documents
    ".pdf": "Documents",
    ".txt": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
}



# Categorises a file into the respective file type folder. (Creating folder if necessary)
def file_categorisation(file, folder_to_organise, dry_run):

    suffix = file.suffix.lower()
    new_folder = False

    if suffix not in SUFFIX_DICT:
        destination = "Others"
    else:
        destination = SUFFIX_DICT[suffix]
        
    destination_path = folder_to_organise / destination

    if not (destination_path.is_dir()):
        new_folder = True

    if(dry_run):
        if (new_folder):
            print(f"{file.name} -> {destination}/ (new)")
            return destination
        print(f"{file.name} -> {destination}/ (new)")
        return destination
    
    if (new_folder):
        destination_path.mkdir()
    shutil.move(file, destination_path)
    return destination
        

def main():

    file_type_count = {
        "Images": 0,
        "Videos": 0,
        "Audio": 0,
        "Compressed": 0,
        "Code": 0,
        "Documents": 0,
        "Others": 0
    }


    print("Python CLI File Organiser!")

    parser = argparse.ArgumentParser(description = "Python CLI File Organiser") 
    parser.add_argument("folder", help = "<- folder to organise")
    parser.add_argument("--dry-run", action = "store_true")
    args = parser.parse_args()
    folder_to_organise = Path(args.folder)


    if not (folder_to_organise.is_dir()):
        print("ERROR: Provided path is not a valid directory.")
        return
    
    for file in folder_to_organise.iterdir():
        if file.is_file():
            file_type_count[file_categorisation(file, folder_to_organise, args.dry_run)] += 1
    
    if (args.dry_run):
        return
    
    print("Categorisation Summary: ")
    for file_type in file_type_count:
        if file_type_count[file_type] == 0:
            continue
        print(f"{file_type}: {file_type_count[file_type]}")
    
    
if __name__ == "__main__":
    main()