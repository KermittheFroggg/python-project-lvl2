def pathGet(dictionary, path):
    for item in path.split("."):
        dictionary = dictionary[item]
    return dictionary


def pathSet(dictionary, path, setItem, signal=None):
    path = path.split(".")
    key = path[-1]
    if len(path) > 1:
        dictionary = pathGet(dictionary, ".".join(path[:-1]))
    if signal == 1:
        dictionary[f'-{key}'] = setItem
    elif signal == 2:
        dictionary[f'+{key}'] = setItem
    else:
        dictionary[key] = setItem


def json_(diff):
    dicty = {}
    for elem in diff:
        if isinstance(elem[2], dict) and isinstance(elem[3], dict):
            pathSet(dicty, elem[1], {})
        elif elem[2] == elem[3]:
            pathSet(dicty, elem[1], elem[2])
        elif elem[2] == 'add':
            pathSet(dicty, elem[1], elem[3], signal=2)
        elif elem[3] == 'rm':
            pathSet(dicty, elem[1], elem[2], signal=1)
        else:
            pathSet(dicty, elem[1], elem[2], signal=1)
            pathSet(dicty, elem[1], elem[3], signal=2)
    return dicty
