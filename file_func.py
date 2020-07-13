import os
import sys
import shutil
from directory_func import create_folder
from filter_func import standardise, remove_error_char


### Functions ---------------

def search(path, keyword):
    content = os.listdir(path)
    result = [None, None, None]  # if no file is found

    for each in content:

        each_path = path + os.sep + each

        # remove all spaces and chinese characters
        each = standardise(each)

        # File or folder found, get directory path
        if keyword == each[:-5] or keyword == each[:-4]:
            # pptx
            if "PPTX" in each:
                result[0] = each_path

            # docx
            elif "DOCX" in each:
                result[1] = each_path
                result[2] = ".docx"

            elif "DOC" in each:
                result[1] = each_path
                result[2] = ".doc"

        # if both lesson plan and ppt is found
        if result[0] != None and result[1] != None:
            return result

        # Recurse deeper into each folder
        if os.path.isdir(each_path) and result[0] is None:
            # not redundant folders
            if each != "Previews" and each != "Demo体验课":
                result = search(each_path, keyword)
                # File found, break all loops
                if result[0] != None or result[1] != None:
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


def missing_slides(teacher, topic, time):
    # create new txt file and write
    if not os.path.exists("missing_ppt.txt"):
        f = open("missing_ppt.txt", "w+", encoding="utf-8")
        f.write("MISSING\n\n" + teacher + ":\t" + time + "--> " + topic + "\n")

    # append onto existing file
    else:
        f = open("missing_ppt.txt", "a+", encoding="utf-8")
        f.write(teacher + ":\t" + time + "--> " + topic + "\n")

    f.close()


def copytree(src, dst, topic, symlinks=False, ignore=None):
    if not os.path.isdir(src) and src.endswith(".pptx"):
        temp = "\\" + topic + ".pptx"
        shutil.copy2(src, dst + temp)

    else:
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)


def add_ppt(src, des, topic):

    try:

        if src[0] is not None:
            shutil.copy2(src[0], des + "\\" + topic + ".pptx")

        if src[1] is not None:
            shutil.copy2(src[1], des + "\\" + topic + src[2])

    except:
        print("error -->", des)


def copy_to_folder(df, root, path):
    # Remove missing_ppt.txt if present
    if os.path.exists("missing_ppt.txt"):
        os.remove("missing_ppt.txt")

    print("Loading in progress: ")

    for index, row in df.iterrows():
        print("=", end="")

        # Directory for sub folders
        topic = remove_error_char(row["Topic"])
        time = remove_error_char(row["Au time"])

        # Teacher Directory
        inner_path = os.path.join(path, row["Teacher"], topic)

        # Filter all invalid chars, find all PowerPoint and Lesson Plan
        filter_topic = standardise(topic)

        # Search for files
        topic_path = search(root, filter_topic)

        # PowerPoint found
        if topic_path[0] is not None:

            # Copy PowerPoints to each respecting teacher
            create_folder(inner_path)
            add_ppt(topic_path, inner_path, topic)

        # Can't locate PowerPoint
        else:
            inner_path = os.path.join(path, row["Teacher"], "MISSING " + topic)
            create_folder(inner_path)
            missing_slides(row["Teacher"], row["Topic"], time)

    print("\nProgram completed\n")
