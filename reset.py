from pathlib import Path
import shutil

# Overarching directories contiaining all sample and test folders.
sample_path = "fixtures/"
test_path = "test_runs/"

# All sample folders.
sample_folder_list = ["basic", "unknown_file"]


# Reset a test folder to a given sample folder.
def reset_test(sample, test):
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
    for sample in sample_folder_list:
        reset_test(f"{sample_path}{sample}_sample", f"{test_path}{sample}_test")

    

if __name__ == "__main__":
    main()