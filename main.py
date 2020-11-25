# This Python script is created to help automate the process of placing the right
# PowerPoint files for each respecting teacher daily at AiEnglish
#
# We are not responsible for any incorrect PowerPoints placed
#
# Created by Andrea Sha, Livy Xu, Shaun Soong, Will Mao
#
# Version 5.2 (updated 20/11/2020)

import os
import pandas as pd

# Custom Functions
from directory_func import create_folder, create_directories, folder_day, get_teachers
from file_func import check_csv, copy_to_folder, choose_dict

### Main ---------------

# Read Airtable CSV, filter irrelevant columns
code_path= "C:\\Users\\Marsha\\Documents\\GitHub\\folder-scripting"     # Code & CSV

src_path = "\\\\10.0.99.99\\PPT\\2.标准化课件 Standardized Courseware"      # PowerPoint Source
des_path = "\\\\10.0.99.99\\PPT\\Presentation\\000Daily folders\\Tomorrow"   # Daily Folder

airtable_csv = check_csv(code_path)
df = pd.read_csv(airtable_csv)
df = df.filter(items=["Teacher", "Topic", "Au time"])
df = df.dropna()
df = df[df.Teacher != "取消"]
df = df[df.Teacher != "取消不计课时"]

# get classes with more than 2 topics per class
index_to_drop = []
for index, row in df.iterrows():
    # find topics with "," meaning it could have double topics
    if row["Topic"].find(",") != -1:
        # find the length, and try to split in a half
        # 2 of the same type of topics should have similar lengths
        topic = row["Topic"]
        length = int(len(topic)/2 - 5)

        # if there is only 1 topic in a array (skip)
        if len(topic[length:].split(",", 1)) == 1:
            continue

        # split from the mid point of the string
        second = topic[length:].split(",", 1)[1]
        mid_index = topic.index(second)
        first = topic[:mid_index-1]

        # check whether it is a double topic class
        # see's the first 2 char (they should have the same subject code)
        first = first.replace('"', '')
        second = second.replace('"', '')

        # topic code that matches
        if first[:2] == second[:2] or second[:2] == "AC":

            # drop current row
            index_to_drop.append(index)
            # append new row into df
            new_df = pd.DataFrame({"Teacher": [row["Teacher"], row["Teacher"]],
                                   "Topic": [first, second],
                                   "Au time": [row["Au time"], row["Au time"]]})
            df = df.append(new_df, ignore_index=True)

df = df.drop(index_to_drop)

# sort by teacher
df = df.sort_values(by=["Teacher"])
df = df.reset_index(drop=True)

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

# reduce dictionary or not
os.chdir(code_path)
# reuse = input("Do you want to reuse dictionary? (press any key for YES; press enter for NO)")
reuse = None
ppt_dict = choose_dict(reuse, 'dictionary.csv', src_path, code_path)


# For each teacher, find all PPTs
os.chdir(daily_folder_path)
copy_to_folder(df, daily_folder_path, ppt_dict)

# End of File
