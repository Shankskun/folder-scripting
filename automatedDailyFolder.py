import os
import pandas as pd
# Custom Functions
from supportFunc import createFolder, createDirectories, folderDay, findCsvFilenames

### Main ---------------

# Read Airtable CSV
# CHANGE THIS
path = 'C:\\Users\\shaunsoong\\Documents\\GitHub\\folder-scripting'
result = findCsvFilenames(path)
df = pd.read_csv(result[0])

# CHANGE THIS
path = "C:\\Users\\shaunsoong\\Desktop\\test"
os.chdir(path)

# Make daily folders based on date
print("[" + result[0] + "] has been used")
whichDay = input("press [ENTER] for today's Daily Folder, [1] for tomorrow's folder:")
day = folderDay(whichDay)

createFolder(day)

# Make teacher folders within today
os.chdir(path + "\\" + day)
createDirectories(df)

# Add PPTs into each folder

