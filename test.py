import os
import shutil
daily_folder_path = "C:\\Users\\livy.xu\\Desktop\\dailyfolder"

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


topic = search (r'Y:\0 标准化课件\2. inclass', 'K1_02_Letters (26 letters).pptx')
print(topic)