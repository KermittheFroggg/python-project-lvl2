import json
import os
import yaml


def boolTolower(file):
    lowerbool = {}
    for key, value in file.items():
        if isinstance(value, bool):
            lowerbool[key] = str(value).lower()
        else:
            lowerbool[key] = value
    return lowerbool


def chooseType(file):
    if os.path.splitext(file)[1] == '.json':
        file = boolTolower(json.load(open(file)))
    elif (os.path.splitext(file)[1] == '.yml') or \
         (os.path.splitext(file)[1] == '.yaml'):
        file = open(file)
        file = boolTolower(yaml.load(file, Loader=yaml.FullLoader))
    return file


def generate_diff(file_path1, file_path2):
    file1 = chooseType(file_path1)
    file2 = chooseType(file_path2)
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
