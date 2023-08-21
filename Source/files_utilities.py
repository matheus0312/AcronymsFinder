"""File management utilities"""
import os
#from main import TEST_MODE

def find_files_in_path(source_path,extensions_expected):
    """Returns all files in input path in a list"""
    found_files = []
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.endswith(tuple(extensions_expected)):
                if True:
                    print(os.path.join(root, file))
                else:
                    found_files.append(os.path.join(root, file))
    return found_files
