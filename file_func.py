import os
import sys
import shutil
import directory_func

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


def standard_topic(topic):
    topic = topic.replace('/', ';')
    topic = topic.replace(':', ' ')
    topic = topic.replace("\n", "")
    topic = topic.replace("\r", "")
    return topic

def add_ppt(topic, src, des):

    shutil.copy2(src, des + topic + ".pptx")


def copy_to_folder(df, root, path):

    # Remove missing_ppt.txt if present
    if os.path.exists("missing_ppt.txt"):
        os.remove("missing_ppt.txt")

    cur_teacher = None

    for index, row in df.iterrows():

        # search for PowerPoint slides
        try:
            topic10 = standard_topic(row["Topic"])
            Path10 = os.path.join(path,row["Teacher"],topic10)
            os.makedirs(Path10)
        except OSError:
            print('Error: Unable to create Directory ->' + row["Teacher"]+"//"+row["Topic"])

        topic_path = search(root, row["Topic"]+'.pptx')
        # PowerPoint found
        if topic_path is not None:

            # Change teacher folders
            if cur_teacher != row["Teacher"]:
                cur_path = path + "\\" + row["Teacher"] + "\\" + topic10 + "\\"

            # Copy PowerPoints to each respecting teacher
            add_ppt(row["Topic"], topic_path, cur_path)

        # Can't locate PowerPoint
        else:
            missing_slides(path, row["Teacher"], row["Topic"])


