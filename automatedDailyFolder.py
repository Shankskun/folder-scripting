import csv
import os
from datetime import date

# Change this for different directories
path = "C:\\Users\\shaunsoong\\Desktop\\test"
os.chdir(path)

# Make folder
new_folder = "Marcus"
os.makedirs(new_folder)

print("hellow")





### --------------------------------------------------- ###


# today = date.today()
# d = today.day
# tomorrow=str(today.replace(day=d+1))
# print(tomorrow)

# def createFolder(directory):
#     try:
#         if not os.path.exists(directory):
#             os.makedirs(directory)
#     except OSError:
#         print('Error: Creating directory. ' + directory)

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
