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
def file_categorisation(file, folder_to_organise):

    suffix = file.suffix.lower()

    if suffix not in SUFFIX_DICT:
        if not ((folder_to_organise / "Others").is_dir()):
            Path(folder_to_organise / "Others").mkdir()
        shutil.move(file, folder_to_organise / "Others")
        return
    
    file_type = SUFFIX_DICT[suffix]


    if not ((folder_to_organise / file_type).is_dir()):
        Path(folder_to_organise / file_type).mkdir()

    shutil.move(file, folder_to_organise / file_type)
    return

        

def main():
    print("Python CLI File Organiser!")

    parser = argparse.ArgumentParser(description = "Python CLI File Organiser") 
    parser.add_argument("folder", help = "<- folder to organise")
    args = parser.parse_args()
    folder_to_organise = Path(args.folder)


    if not (folder_to_organise.is_dir()):
        print("ERROR: Provided path is not a valid directory.")
        return
    
    for file in folder_to_organise.iterdir():
        if not file.is_dir():
            file_categorisation(file, folder_to_organise)
            

    
    
if __name__ == "__main__":
    main()