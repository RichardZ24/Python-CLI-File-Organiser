from pathlib import Path
import argparse
import shutil

#python3 main.py ~/test_folder_basic

suffix_dict = {
    ".jpeg": "Images",
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".aac": "Audio",
    ".zip": "Compressed",
    ".rar": "Compressed",
    ".7z": "Compressed",
    ".gz": "Compressed",
    ".tar": "Compressed",
}


# Operations:
# given a suffix and folder to organise, check if the suffix already has a directory created for it, if it has, return true, else return false

def dir_exists(suffix, folder_to_organise):
    dir_list = []
    for item in folder_to_organise.iterdir():
        if item.is_dir():
            dir_list.append(item)
    

        

def main():
    print("Python CLI File Organiser!")

    parser = argparse.ArgumentParser(description = "Python CLI File Organiser") 

    #arguments needed
    parser.add_argument("folder", help = "<- folder to organise")

    args = parser.parse_args()
    folder_to_organise = Path(args.folder)

    if not (folder_to_organise.is_dir()):
        print("ERROR: Provided path is not a valid directory.")
        return
    
    for file in folder_to_organise.iterdir():
        suffix = file.suffix
        match suffix:
            case ".jpg":
                if dir_exists(suffix, folder_to_organise):
                    shutil.move(file, folder_to_organise / "Images" / file.name)
                else:
                    Path(folder_to_organise / "Images").mkdir(exist_ok=True)
                    shutil.move(file, folder_to_organise / "Images" / file.name)


    
    
if __name__ == "__main__":
    main()