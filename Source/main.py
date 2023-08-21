"""Main function"""

# test variables
TEST_MODE = True

# pyperclip makes it possible to use copy/paste to input/output data in the code 
#import pyperclip

# import local functions
import files_utilities
print('Acronyms Finder SW')

if not TEST_MODE:
    print('What is the source path to be considered?')
    source_path = input()
    print('What are the file extensions to be considered?')
    source_path = input()
else:
    source_path = '/workspaces/AcronymsFinder/'
    extensions_expected = ['.txt', '.py']

# find applicable files in root folder
files_utilities.find_files_in_path(source_path, extensions_expected)

# verifies which files should be considered

# iterate over files to identify acronyms

# checks found acronyms against dictionaries

# checks files for dictionary acronyms not found

# prints to user acronyms found (new, ignored, known)