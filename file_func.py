import os
import sys
import shutil
from directory_func import create_folder


### Functions ---------------


def search(path, keyword):
    content = os.listdir(path)
    result = None  # if no file is found

    keyword = keyword.replace(" ", "").replace("_", "").replace("-", "")
    keyword = keyword.replace("（", "(").replace("）", ")")
    keyword = keyword.replace("V4.0", "").replace("V4.0", "")
    def vdect(each):
        m = [i for i in range(10)]
        n = [i for i in range(10)]
        version = []
        for i in range(10):
            for j in range(10):
                version.append(f'V{i}.{j}')
        for elem in version:
            if elem in each:
                each.replace(elem, '')
            else:
                pass
    for each in content:

        each_path = path + os.sep + each

        # remove all spaces and chinese characters
        each = each.replace(" ", "").replace("_", "").replace("-", "")
        each = each.replace("（", "(").replace("）", ")")
        each = each.replace("V4.0", "").replace("V4.0", "")
        each = each.replace(".pptx", "").replace("°Ø", "").replace("’", '')
        # each = vdect(each)
        # File or folder found, get directory path
        if keyword == each and not (each.endswith(".docx") or each.endswith(".doc")):
            result = each_path
            return result
        # Recurse deeper into each folder
        if os.path.isdir(each_path):
            # not redundant folders
            if each != "Previews" and each != "Demo体验课":
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
        copytree(src, des, topic)

    except OSError:
        print("\npotential error ->", des)


def copy_to_folder(df, root, path):
    # Remove missing_ppt.txt if present
    if os.path.exists("missing_ppt.txt"):
        os.remove("missing_ppt.txt")

    print("Loading in progress: ")

    for index, row in df.iterrows():
        print("=", end="")

        # Directory for sub folders
        time = standard_topic(row["Au time"])
        topic = standard_topic(row["Topic"])

        # Teacher Directory
        inner_path = os.path.join(path, row["Teacher"], topic)

        # Find all PowerPoint and Lesson Plan
        topic_path = search(root, row["Topic"])

        # PowerPoint found
        if topic_path is not None:

            # Copy PowerPoints to each respecting teacher
            # add_ppt(topic_path, inner_path + "\\" + topic)
            create_folder(inner_path)
            add_ppt(topic_path, inner_path, topic)

        # Can't locate PowerPoint
        else:
            inner_path = os.path.join(path, row["Teacher"], "MISSING " + topic)
            create_folder(inner_path)
            missing_slides(row["Teacher"], row["Topic"], time)

    print("\nProgram completed\n")

    # # if directory is empty
    # try:
    #     if not os.listdir(inner_path):
    #         # search for PowerPoint slides
    #         # topic_path = search(root, row["Topic"] + ".pptx")
    #         topic_path = search(root, row["Topic"])
    #
    #         # PowerPoint found
    #         if topic_path is not None:
    #
    #             # Copy PowerPoints to each respecting teacher
    #             add_ppt(topic_path, inner_path + "\\" + topic)
    #
    #         # Can't locate PowerPoint
    #         else:
    #             missing_slides(row["Teacher"], row["Topic"], time)
    #
    # except OSError:
    #     print("error checking inner folder")
