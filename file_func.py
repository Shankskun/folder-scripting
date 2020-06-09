import os
import sys
import shutil
from directory_func import create_folder

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
                # result = result.replace("\\", "\\\\")
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


def missing_slides(path, teacher, topic):
    # create new txt file and write
    if not os.path.exists("missing_ppt.txt"):
        f = open("missing_ppt.txt", "w+", encoding="utf-8")
        f.write("MISSING\n\n" + teacher + "\t --> " + topic + "\n")

    # append onto existing file
    else:
        f = open("missing_ppt.txt", "a+", encoding="utf-8")
        f.write(teacher + "\t --> " + topic + "\n")

    f.close()


def add_ppt(topic, src, des):
    shutil.copy2(src, des + topic + ".pptx")


def copy_to_folder(df, root, path):
    # Remove missing_ppt.txt if present
    if os.path.exists("missing_ppt.txt"):
        os.remove("missing_ppt.txt")

    cur_teacher = None

    for index, row in df.iterrows():

        # search for PowerPoint slides
        topic_path = search(root, row["Topic"])

        # PowerPoint found
        if topic_path is not None:

            # Change teacher folders
            if cur_teacher != row["Teacher"]:
                cur_path = path + "\\" + row["Teacher"] + "\\"

            # Copy PowerPoints to each respecting teacher
            create_folder(row["Topic"])
            add_ppt(row["Topic"], topic_path, cur_path + "\\" + row["Topic"])

        # Can't locate PowerPoint
        else:
            missing_slides(path, row["Teacher"], row["Topic"])
