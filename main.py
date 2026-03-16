from pathlib import Path
import argparse

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

    
    
if __name__ == "__main__":
    main()