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
            # not redundant folders
            if each != "Previews" and each != "Demo 体验课":
                result = search(each_path, keyword)
                # File found, break all loops
                if result is not None:
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


def standard_topic(topic):
    topic = topic.replace("/", ";")
    topic = topic.replace(":", "")
    topic = topic.replace("\n", "")
    topic = topic.replace("\r", "")

    return topic


def add_ppt(src, des):
    shutil.copy2(src, des + ".pptx")


def copy_to_folder(df, root, path):
    # Remove missing_ppt.txt if present
    if os.path.exists("missing_ppt.txt"):
        os.remove("missing_ppt.txt")

    cur_teacher = None
    topic_path = None

    print("Loading in progress: ")

    for index, row in df.iterrows():
        print("=", end="")

        # Directory for sub folders
        time = standard_topic(row["Au time"])
        topic = standard_topic(row["Topic"])

        inner_path = os.path.join(path, row["Teacher"], topic)
        # inner_path = os.path.join(path, row["Teacher"], time)

        create_folder(inner_path)

        # if directory is empty
        try:
            if not os.listdir(inner_path):
                # search for PowerPoint slides
                topic_path = search(root, row["Topic"] + ".pptx")

                # PowerPoint found
                if topic_path is not None:

                    # Change teacher folders
                    if cur_teacher != row["Teacher"]:
                        # cur_path = path + "\\" + row["Teacher"] + "\\" + time
                        cur_path = path + "\\" + row["Teacher"] + "\\" + topic

                    # Copy PowerPoints to each respecting teacher
                    add_ppt(topic_path, cur_path + "\\" + topic)

                    # # Find Lesson plan (docx)
                    # doc_path = strip_end(topic_path, topic + ".pptx")
                    # doc_path = search(root, row["Topic"] + ".docx")
                    #
                    # if doc_path is not None:
                    #     add_ppt(doc_path, cur_path + "\\" + topic)

                # Can't locate PowerPoint
                else:
                    missing_slides(row["Teacher"], row["Topic"], time)

        except OSError:
            print("error checking inner folder")
