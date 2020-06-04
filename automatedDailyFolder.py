import os
import csv
import pandas as pd
from datetime import date
import shutil
### Functions
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Unable to create Directory ->' + directory)

def search(path,keyword):
	content= os.listdir(path)
	for each in content:
		each_path = path+os.sep+each
		if keyword in each:
			print(each_path)
		if os.path.isdir(each_path):
			search(each_path,keyword)
result = search(r'C:\0 标准化课件\2. inclass','BF2_U1 My School_L4_(20+20)')
if result == "":
	print("cannot find" + topic_list)
else:
	shutil.copy2(result, newpath)
### Main

# Change this for different directories
path = "C:\\Users\\shaunsoong\\Desktop\\test"
os.chdir(path)

# Make folder
createFolder("yo")

trainData = pd.read_csv('test.csv')
teacher = trainData.iloc[:, 4]
teacher_list = teacher.values.tolist()
topic = trainData.iloc[:, 3]
teacher_listclean = list(set(teacher_list))
print(teacher_listclean)
i=0
while i<len(teacher_listclean):
    os.makedirs(teacher_listclean[i])
    i = i+1
teacher = trainData.iloc[:, 3]





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
