# Python-CLI-File-Organiser
A Python command-line tool built using pathlib, argparse and shutil.

## Features
- Accepts a path to a directory as a command line argument.
- Categorises all files in the directory into sub-directories based on the file extension.
- Creates sub-directories if they do not already exist.
- Has reset script for testing purposes.

## Layout
```
Python CLI File Organiser/
    fixtures/
        basic_sample/
        unknown_file_sample
    test_runs/
        basic_test/
        unknown_file_test/
    organise.py
    README.md
    reset_test_folder.py
```

## Usage
```
python3 organise.py ~/test_folder_basic
python3 reset_test_folder.py
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
    Unknown/
        unknown_file_type.kfasdoi
```
## Future Improvements
- Dry run mode
- Undo support
- Duplicate file name handling
- Recursive directory support
- Tidier change-log for user

## Git Development Notes
- Developed using incremental Git commits following conventional commit messages.


