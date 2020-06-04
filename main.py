import os
import shutil
import pandas as pd

# Custom Functions
from support_func import create_folder, create_directories, folder_day, search
from check_func import checkCsv

### Main ---------------

# Read Airtable CSV
# CHANGE THIS
path = 'C:\\Users\\shaunsoong\\Documents\\GitHub\\folder-scripting'
result = checkCsv(path)
df = pd.read_csv(result)

# CHANGE THIS
path = "C:\\Users\\shaunsoong\\Desktop\\test"
os.chdir(path)





# Make daily folders based on date
print("[" + result + "] has been used")
whichDay = input("press [ENTER] for today's Daily Folder, [1] for tomorrow's folder:")
day = folder_day(whichDay)

create_folder(day)

# Make teacher folders within today
os.chdir(path + "\\" + day)
create_directories(df)

# Add PPTs into each folder



