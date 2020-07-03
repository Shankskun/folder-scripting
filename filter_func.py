### Global Var ---------------

non_allowed_char = [" ", "_", "-", "(", ")", "（", "）", ":", "~", ".pptx",
                    "°Ø", "’", "©", "®", "£", "+", "+", "：", ": ", " ", " "]
  
n = [i for i in range(10)]
m = n.copy()
lst = []
for i in n:
    for j in m:
        lst.append(f'V{i}.{j}')


### Functions ---------------


def vdetect(name):
    for i in range(4, len(name)):
        elem = name[i - 4: i]
        if elem in lst:
            name = name[:i - 4] + name[i:]
    return name


def numberdect(name):
    if name[0].isdigit():
        return numberdect(name[1:])
    elif name[:4] == "JNCE":
        return numberdect(name[4:])
    else:
        return name


def sytaxdect(name):
    if name[-1] == '.':
        return name[:-1]
    name = name.upper()
    name = name.replace("COLOR", "COLOUR")
    name = name.replace("  ", '')
    name = name.replace(" ", '')
    return name


def standardise(word):

    for i in non_allowed_char:
        word = word.replace(i, "")

    return word
