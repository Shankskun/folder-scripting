import os


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
