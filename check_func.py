import sys
from supportFunc import createFolder, createDirectories, folderDay, findCsvFilenames

### Functions ---------------

def checkCsv(path):
    result = findCsvFilenames(path)

    if result:
        return result[0]

    print("No CSV found, please place one in this folder")
    sys.exit()
