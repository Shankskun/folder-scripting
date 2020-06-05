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
from directory_func import create_folder, create_directories, folder_day, get_teachers, add_ppt
from file_func import search, check_csv

### Main ---------------

# CHANGE THIS
# Read Airtable CSV
path = "C:\\Users\\shaunsoong\\Documents\\GitHub\\folder-scripting"

airtable_csv = check_csv(path)
df = pd.read_csv(airtable_csv)

# CHANGE THIS
# Daily Folder Location
path = "C:\\Users\\shaunsoong\\Desktop\\test"
os.chdir(path)

# Make daily folders based on date
print("[" + airtable_csv + "] has been used")
whichDay = input("press [ENTER] for today's Daily Folder, [1] for tomorrow's folder:")

day = folder_day(whichDay)
create_folder(day)

# Make teacher folders
teachers = get_teachers(df)
# FIND PPT
ppt = search(path, "我们")


daily_folder = path + "\\" + day
os.chdir(daily_folder)
create_directories(teachers, ppt, path)

# Add PPTs into each
print(daily_folder)
add_ppt(teachers, ppt, daily_folder)


