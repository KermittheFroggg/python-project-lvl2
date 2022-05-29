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


def generate_diff(file_path1, file_path2):
    if os.path.splitext(file_path1)[1] == '.json':
        file1 = boolTolower(json.load(open(file_path1)))
    elif (os.path.splitext(file_path1)[1] == '.yml') or \
        (os.path.splitext(file_path1)[1] == '.yaml'):
        file1 = open(file_path1)
        file1 = boolTolower(yaml.load(file1, Loader=yaml.FullLoader))
    if os.path.splitext(file_path1)[1] == '.json':
        file2 = boolTolower(json.load(open(file_path2)))
    elif (os.path.splitext(file_path1)[1] == '.yml') or \
        (os.path.splitext(file_path1)[1] == '.yaml'):
        file2 = open(file_path2)
        file2 = boolTolower(yaml.load(file2, Loader=yaml.FullLoader))
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
