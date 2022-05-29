import json


def boolTolower(file):
    lowerbool = {}
    for key, value in file.items():
        if isinstance(value, bool):
            lowerbool[key] = str(value).lower()
        else:
            lowerbool[key] = value
    return lowerbool


def generate_diff(file_path1, file_path2):
    file1 = boolTolower(json.load(open(file_path1)))
    file2 = boolTolower(json.load(open(file_path2)))
    print(file1)
    source = ''
    for elem in (set(file1) - set(file2)):
        source += f'\n  - {elem}: {file1[elem]}'
    for elem in (set(file1) & set(file2)):
        if file1[elem] == file2[elem]:
            source += f'\n    {elem}: {file1[elem]}'
        else:
            source += f'\n  - {elem}: {file1[elem]}\n  + {elem}: {file2[elem]}'
    for elem in (set(file2) - set(file1)):
        source += f'\n  + {elem}: {file2[elem]}'
    source = '{' + source + '\n' + '}'
    return source
