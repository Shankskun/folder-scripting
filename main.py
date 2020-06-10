# This Python script is created to help automate the process of placing the right
# PowerPoint files for each respecting teacher daily at AiEnglish
#
# We are not responsible for any incorrect PowerPoints placed
#
# Created by Andrea Sha, Livy Xu, Shaun Soong
#
# Version 1.0 Beta

import os
import pandas as pd

# Custom Functions
from directory_func import create_folder, create_directories, folder_day, get_teachers
from file_func import check_csv, copy_to_folder

### Main ---------------

# CHANGE THIS
# Read Airtable CSV, filter irrelevant columns
root_path = "C:\\Users\\livy.xu\\Desktop\\test"          # Presentation Folder on dc01
path = "C:\\Users\\livy.xu\\Documents\\GitHub\\folder-scripting"
daily_folder_path = "C:\\Users\\livy.xu\\Desktop\\dailyfolder"


airtable_csv = check_csv(path)
df = pd.read_csv(airtable_csv)
df = df.filter(items=["Teacher", "Topic"])
df = df.sort_values(by=["Teacher"])
df = df.dropna()

# remove CSV used
# os.remove(airtable_csv)

# Daily Folder Location
os.chdir(root_path)

# Make daily folders based on date
print("[" + airtable_csv + "] has been used")
whichDay = input("press [ENTER] for today's Daily Folder, [1] for tomorrow's folder:")

day = folder_day(whichDay)
create_folder(day)

# Make teacher folders
teachers = get_teachers(df)

daily_folder_path = root_path + "\\" + day
os.chdir(daily_folder_path)
create_directories(teachers)

# For each teacher, find all PPTs
copy_to_folder(df, r'Y:\0 标准化课件\2. inclass', daily_folder_path)

# End of File
