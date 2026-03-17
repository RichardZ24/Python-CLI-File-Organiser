# Python-CLI-File-Organiser
A Python command-line tool built using pathlib, argparse and shutil.

## Features
- Accepts a path to a directory as a command line argument.
- Categorises all files in the directory into sub-directories based on the file extension.
- Creates sub-directories if they do not already exist.
- Can preview file structure with a flag
- Prints a categorisation summary upon completion
- Has reset script for testing purposes.

## Layout
```
Python CLI File Organiser/
    fixtures/
        basic_sample/
        empty_sample/
        existing_folder_sample/
        nested_directory_sample/
        no_extension_sample/
        unknown_file_sample/
        uppercase_extension_sample/
    test_runs/
        basic_test/
        empty_test/
        existing_folder_test/
        nested_directory_test/
        no_extension_test/
        unknown_file_test/
        uppercase_extension_test/
    organise.py
    README.md
    reset.py
```

## Usage
```
python3 organise.py ~/basic_test
python3 organise.py ~/basic_test --dry-run
python3 reset.py
```


## Example
Before:
```
Downloads/
    compressed_file.zip
    python_script.py
    assignment1.pdf
    assignment2.pdf
    unknown_file_type.kfasdoi
    image.png
    image2.jpg
```
After:
```
Downloads/
    Compressed/
        compressed_file.zip
    Code/
        python_script.py
    Documents/
        assignment1.pdf
        assignment2.pdf
    Images/
        image.png
        image2.jpg
    Others/
        unknown_file_type.kfasdoi
```
## Future Improvements
- Undo support
- Duplicate file name handling
- Recursive directory support
- Add further automation features for reset script (all flag, automatically includes new samples, individual test case reset)

## Git Development Notes
- Developed using incremental Git commits following conventional commit messages.


