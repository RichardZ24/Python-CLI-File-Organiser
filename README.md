# Python-CLI-File-Organiser
A Python command-line tool built using pathlib, argparse and shutil.

## Features
- Accepts a path to a directory as a command line argument.
- Categorises all files in the directory into sub-directories based on the file extension.
- Creates sub-directories if they do not already exist.
- Prints a categorisation summary upon completion
- Has reset script for testing purposes.

## Layout
```
Python CLI File Organiser/
    fixtures/
        basic_sample/
        unknown_file_sample/
    test_runs/
        basic_test/
        unknown_file_test/
    organise.py
    README.md
    reset.py
```

## Usage
```
python3 organise.py ~/basic_test
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
- Dry run mode
- Undo support
- Duplicate file name handling
- Recursive directory support

## Git Development Notes
- Developed using incremental Git commits following conventional commit messages.


