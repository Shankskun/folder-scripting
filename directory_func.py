import os
import sys
import shutil
import datetime
from datetime import date


### Functions ---------------

def check_csv(path):
    result = find_csv_filename(path)

    if result:
        return result[0]

    print("No CSV found, please place one in this folder")
    sys.exit()


def folder_day(entered_day):
    if entered_day == '':
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


def create_directories(df, ppt, path):
    # for all teachers, make a folder
    teachers = get_teachers(df)

    for i in teachers:
        cur_dr = path
        # remove empty values
        if str(i) != 'nan':
            create_folder(str(i))
            cur_dr = path + "\\" + i + "test.pptx"
            print("cur->", (cur_dr))
            print(ppt)
            shutil.copyfile(ppt, cur_dr)

    return 0


def find_csv_filename(path_to_dir, suffix=".csv"):
    filenames = os.listdir(path_to_dir)
    return [filename for filename in filenames if filename.endswith(suffix)]
