from pathlib import Path
import argparse
import shutil


def main():

    for file in Path("test_runs/test_folder_basic").iterdir():
        if (file.is_dir()):
            shutil.rmtree(file)
        else:
            file.unlink()
    for file in Path("fixtures/sample_test_folder").iterdir():
        shutil.copy(file, Path("test_runs/test_folder_basic"))

if __name__ == "__main__":
    main()