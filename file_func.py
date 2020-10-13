import os
import sys
import shutil
from directory_func import create_folder
from filter_func import standardise, remove_error_char


### Functions ---------------

def build_dict(path):
    content = os.listdir(path)
    dict = {}

    for each in content:

        print("=", end="")
        each_path = path + os.sep + each
                
        # dont read redundant folders
        if each != "4.live" and each != "5.preview" and each != "6.opening class" and each != "7.topics":

        # remove all spaces and chinese characters
        each = standardise(each)

        # Recurse deeper into each folder
        if os.path.isdir(each_path):
            temp_dict = build_dict(each_path)
            dict.update(temp_dict)
            
        # store file into dict
        else:
            dict[each] = each_path

    return dict


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


def add_ppt(src, des, topic):

    try:

        if src[0] is not None:
            shutil.copy2(src[0], des + "\\")

        if src[2] is not None:
            shutil.copy2(src[2], des + "\\" + topic + "_LP" + src[3])

    except:
        print("error -->", des)


def copy_to_folder(df, path, ppt_dict):
    # Remove missing_ppt.txt if present
    if os.path.exists("missing_ppt.txt"):
        os.remove("missing_ppt.txt")

    print("\n\nCopying Files: \n")

    for index, row in df.iterrows():
        print("=", end="")

        # Teacher Directory
        inner_path = os.path.join(path, row["Teacher"], topic)

        # Filter all invalid chars, find all PowerPoint and Lesson Plan
        filter_topic = standardise(topic)

        # Find ppt and LP
        src = [None, None, None, None]

        if (filter_topic + "PPTX") in ppt_dict.keys():
            # PowerPoint
            src[0] = ppt_dict[filter_topic + "PPTX"]
            src[1] = ".pptx"

            # Word
            if (filter_topic + "DOC") in ppt_dict.keys():
                src[2] = ppt_dict[filter_topic + "DOC"]
                src[3] = ".doc"
            elif (filter_topic + "DOCX") in ppt_dict.keys():
                src[2] = ppt_dict[filter_topic + "DOCX"]
                src[3] = ".docx"

        # Put in folder
        if src[0] is not None:
            create_folder(inner_path)
            add_ppt(src, inner_path, topic)
        # cant find file
        else:
            inner_path = os.path.join(path, row["Teacher"], "MISSING " + topic)
            create_folder(inner_path)
            missing_slides(row["Teacher"], row["Topic"], time)

    print("\nProgram completed\n")
