import os
import datetime
from datetime import date

### Functions ---------------

def folderDay(enteredDay):
    if (enteredDay == ''):
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


def findCsvFilenames(path_to_dir, suffix=".csv"):
    filenames = os.listdir(path_to_dir)
    return [filename for filename in filenames if filename.endswith(suffix)]
