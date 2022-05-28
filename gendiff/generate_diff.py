import json


def generate_diff(file_path1, file_path2):
    file1 = json.load(open(file_path1))
    file2 = json.load(open(file_path2))
    source = ''
    for elem in (set(file1) - set(file2)):
        source += f'\n - {elem}: {file1[elem]}'
    for elem in (set(file1) & set(file2)):
        if file1[elem] == file2[elem]:
            source += f'\n   {elem}: {file1[elem]}'
        else:
            source += f'\n - {elem}: {file1[elem]}\n + {elem}: {file2[elem]}'
    for elem in (set(file2) - set(file1)):
        source += f'\n + {elem}: {file2[elem]}'
    source = '{' + source + '\n' + '}'
    return source
