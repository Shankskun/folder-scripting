import os
import sys
import shutil


### Functions ---------------

def search(path, keyword):
    content = os.listdir(path)
    result = None  # if no file is found

    for each in content:
        each_path = path + os.sep + each
        # File found, get directory path
        if keyword in each:
            result = each_path
            return result
        # Recurse
        if os.path.isdir(each_path):
            result = search(each_path, keyword)
            # File found, break all loops
            if result is not None:
                result = result.replace("\\", "\\\\")
                break

    return result


def find_csv_filename(path_to_dir, suffix=".csv"):
    filenames = os.listdir(path_to_dir)
    return [filename for filename in filenames if filename.endswith(suffix)]


def check_csv(path):
    result = find_csv_filename(path)

    # find the only CSV file within the directory
    if result:
        return result[0]

    print("No CSV found, please place one in this folder")
    sys.exit()


def add_ppt(topic, root, des):

    for i in teachers:

        if str(i) != "":
            teacher_dr = des + "\\" + str(i) + "\\" + "test.pptx"
            shutil.copy2(src, teacher_dr)


def copy_to_folder(df, root, path):

    cur_teacher = None

    for index, row in df.iterrows():

        # change teacher directory
        if cur_teacher != row["Teacher"]:
            cur_path = path + "\\" + row["Teacher"] + "\\" + row["Teacher"] + "\\"
            add_ppt(row["Topic"], cur_path)

        # retain the same directory
        else:
            add_ppt(row["Topic"])

