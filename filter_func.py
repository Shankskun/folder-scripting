### Global Var ---------------

non_allowed_char = ["_LP", " ", "_", "-", "(", ")", "（", "）", ":", "~",  " ", " ", "?", "？", "  ", " ",
                    "°Ø", "’", "©", "®", "£", "+", "+", "：", ": ", "，", "。", "、"]
  
n = [i for i in range(10)]
m = n.copy()
lst = []
for i in n:
    for j in m:
        lst.append(f'V{i}.{j}')


### Functions ---------------


def remove_error_char(word):

    word = word.replace(":", "").replace("\\", "").replace("/", "").replace("\n", "").replace(" ", " ")

    if word[len(word)-1] == " ":
        word = word[:-1]

    return word


# removes Version from name, ie V4.0 etc
def vdetect(name):

    if len(name) > 0:
        for i in range(4, len(name)):
            elem = name[i - 4: i]
            if elem in lst:
                name = name[:i - 4] + name[i:]
    return name


# removes random numbers placed
def numberdect(name):
    if len(name) > 0:
        if name[0].isdigit():
            return numberdect(name[1:])
        elif name[:4] == "JNCE":
            return numberdect(name[4:])
        else:
            return name
    return name


# standardise the syntax
def sytaxdect(name):
    if len(name) > 0:

        if name[-1] == '.':
            return name[:-1]

        name = name.upper()
        name = name.replace("COLOR", "COLOUR")

    return name


# remove more random stuff
def standardise(word):

    word = numberdect(word)

    for i in non_allowed_char:
        word = word.replace(i, "")

    word = vdetect(word)
    word = sytaxdect(word)

    return word
