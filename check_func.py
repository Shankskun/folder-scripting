import sys
from support_func import create_folder, create_directories, folder_day, find_csv_filenames

### Functions ---------------

def checkCsv(path):
    result = find_csv_filenames(path)

    if result:
        return result[0]

    print("No CSV found, please place one in this folder")
    sys.exit()
