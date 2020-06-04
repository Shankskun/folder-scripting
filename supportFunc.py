import os
import datetime
from datetime import date

import pandas as pd

### Functions ---------------

def folderDay(enteredDay):
    if(enteredDay == ''):
        day = date.today()
        day = str(day)
    else:
        day = date.today()
        day = str(day + datetime.timedelta(days=1))

    print(day + "'s folder has been created!")
    return day


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
        # remove empty values
        if str(i) != 'nan':
            createFolder(str(i))

    return 0
