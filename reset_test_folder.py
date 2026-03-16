from pathlib import Path
import argparse
import shutil

def reset_test_folder(sample, test):

    if not Path(test).is_dir():
        Path(test).mkdir()

    for file in Path(test).iterdir():
        if (file.is_dir()):
            shutil.rmtree(file)
        else:
            file.unlink()
    for file in Path(sample).iterdir():
        shutil.copy(file, Path(test))

def main():
    reset_test_folder("fixtures/basic_test_sample", "test_runs/basic_test")
    reset_test_folder("fixtures/unknown_file_sample", "test_runs/unknown_file_test")

    

if __name__ == "__main__":
    main()