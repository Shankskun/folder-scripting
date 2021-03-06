import os
import datetime
from datetime import date


### Functions ---------------


def folder_day(entered_day):
    if entered_day == '':
        day = date.today()
    else:
        day = datetime.datetime(date.today().year, date.today().month, int(entered_day))

    day = str(day.strftime('%d-%b-%Y'))
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


def create_directories(teachers):

    for i in teachers:

        # remove empty values
        if str(i) != "":
            create_folder(str(i))

    return 0





