import os
import pandas as pd


### Functions
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Unable to create Directory ->' + directory)


def getTeachers(df):
    # get all teachers, and remove duplicates
    teachers = df.Teacher.tolist()
    teachers = list(dict.fromkeys(teachers))

    return teachers


def createDirectories(df):
    # for all teachers, make a folder
    teachers = getTeachers(df)

    for i in teachers:
        createFolder(str(i))

    return 0
