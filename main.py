# This Python script is created to help automate the process of placing the right
# PowerPoint files for each respecting teacher daily at AiEnglish
#
# We are not responsible for any incorrect PowerPoints placed
#
# Created by Andrea Sha, Livy Xu, Shaun Soong, Will Mao
#
# Version 4.0 (updated 14/7/2020)

import os
import pandas as pd

# Custom Functions
from directory_func import create_folder, create_directories, folder_day, get_teachers
from file_func import check_csv, copy_to_folder

### Main ---------------

# Read Airtable CSV, filter irrelevant columns
code_path= "C:\\Users\\shaunsoong\\Documents\\GitHub\\folder-scripting"     # Code & CSV
src_path = "\\\\10.0.99.99\\ppt\\0 标准化课件\\2. inclass"      # PowerPoint Source
des_path = "\\\\10.0.99.99\\ppt\\Presentation\\000Daily folders"   # Daily Folder
# des_path = "C:\\Users\\shaunsoong\\Desktop\\Test"   # Daily Folder

airtable_csv = check_csv(code_path)
df = pd.read_csv(airtable_csv)
df = df.filter(items=["Teacher", "Topic", "Au time"])
df = df.sort_values(by=["Teacher"])
df = df.dropna()
df = df[df.Teacher != "取消"]

# remove CSV used
# os.remove(airtable_csv)

# Daily Folder Location
os.chdir(des_path)

# Make daily folders based on date
print("[" + airtable_csv + "] has been used")
whichDay = input("press [ENTER] for TODAY, or type in the day (ie '23' for 23-month) :")

day = folder_day(whichDay)
create_folder(day)

# Make teacher folders
teachers = get_teachers(df)

daily_folder_path = des_path + "\\" + day
os.chdir(daily_folder_path)
create_directories(teachers)

# For each teacher, find all PPTs
copy_to_folder(df, src_path, daily_folder_path)

# End of File
