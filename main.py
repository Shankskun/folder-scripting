# This Python script is created to help automate the process of placing the right
# PowerPoint files for each respecting teacher daily at AiEnglish
#
# We are not responsible for any incorrect PowerPoints places
#
# Created by Andrea Sha, Livy Xu, Shaun Soong
#
# Version 1.0 Beta

import os
import pandas as pd

# Custom Functions
from directory_func import create_folder, create_directories, folder_day, check_csv
from file_func import search

### Main ---------------

# Read Airtable CSV
# CHANGE THIS
path = "C:\\Users\\shaunsoong\\Documents\\GitHub\\folder-scripting"
result = check_csv(path)
df = pd.read_csv(result)

# CHANGE THIS
path = "C:\\Users\\shaunsoong\\Desktop\\test"
os.chdir(path)

# FIND PPT
ppt = search(path, "ppt1")


# Make daily folders based on date
print("[" + result + "] has been used")
whichDay = input("press [ENTER] for today's Daily Folder, [1] for tomorrow's folder:")
day = folder_day(whichDay)

create_folder(day)

# Make teacher folders within today
os.chdir(path + "\\" + day)
create_directories(df, ppt, path)



# Add PPTs into each folder



