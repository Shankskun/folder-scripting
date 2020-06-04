import os
import datetime
from datetime import date


### Functions ---------------

def folder_day(enteredDay):
    if (enteredDay == ''):
        day = date.today()
        day = str(day)
    else:
        day = date.today()
        day = str(day + datetime.timedelta(days=1))

    print(day + "'s folder has been created!")
    return day


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Unable to create Directory ->' + directory)


def get_teachers(df):
    # get all teachers, and remove duplicates
    teachers = df.Teacher.tolist()
    teachers = list(dict.fromkeys(teachers))

    return teachers


def create_directories(df):
    # for all teachers, make a folder
    teachers = get_teachers(df)

    for i in teachers:
        # remove empty values
        if str(i) != 'nan':
            create_folder(str(i))

    return 0


def find_csv_filenames(path_to_dir, suffix=".csv"):
    filenames = os.listdir(path_to_dir)
    return [filename for filename in filenames if filename.endswith(suffix)]


def search(path, keyword):
    content = os.listdir(path)
    for each in content:
        each_path = path + os.sep + each
        if keyword in each:
            print(each_path)
        if os.path.isdir(each_path):
            search(each_path, keyword)
