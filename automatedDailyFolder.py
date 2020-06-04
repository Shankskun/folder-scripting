import os
import csv
import pandas as pd
from datetime import date

# Custom Functions
from supportFunc import createFolder, createDirectories, folderDay

### Main ---------------

# Read Airtable CSV
df = pd.read_csv('timetable.csv')

# Change this for different directories
path = "C:\\Users\\shaunsoong\\Desktop\\test"
os.chdir(path)

# Make daily folders based on date
whichDay = input("[ENTER] for today's Daily Folder, [1] for tomorrow's folder:")
day = folderDay(whichDay)


createFolder(day)

# Make teacher folders within today
os.chdir(path + "\\" + day)
createDirectories(df)
















# teacher_list = teacher.values.tolist()
# topic = trainData.iloc[:, 3]
# teacher_listclean = list(set(teacher_list))
# print(teacher_listclean)
# i=0
# while i<len(teacher_listclean):
#     os.makedirs(teacher_listclean[i])
#     i = i+1
# teacher = trainData.iloc[:, 3]





### --------------------------------------------------- ###


# today = date.today()
# d = today.day
# tomorrow=str(today.replace(day=d+1))
# print(tomorrow)


# def findFile(name, path):
#     for root, dirs, files in os.walk(path):
#         if name in files:
#             return os.path.join(root, name)

# with open('schedule.csv', newline="", encoding='utf-8') as f:
#     reader = csv.reader(f)
#     os.chdir("Y:/000Daily folders")
#     createFolder(tomorrow)
#     os.chdir("Y:/000Daily folders/" + tomorrow)
#     for row in reader:
#         teacher = row[5]
#         #createFolder(teacher)
#         topic = str(row[4].strip())
#         new_topic = "".join(topic.split())
#         file = findFile("ZHFLS_G4_03_Lily the Cat_L2.ppt", "Y:/0 标准化课件")
#         #print(repr(new_topic))
