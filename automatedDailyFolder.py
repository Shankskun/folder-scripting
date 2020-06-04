import os
import csv
import pandas as pd
from datetime import date


### Functions
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Unable to create Directory ->' + directory)



### Main

# Change this for different directories
path = "C:\\Users\\shaunsoong\\Desktop\\test"
os.chdir(path)

# Make folder
createFolder("yo")







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
