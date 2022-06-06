import json
import os
import yaml
from gendiff.stylish import stylish


def boolTolower(file):
    def inner(node):
        for key, value in node.items():
            if isinstance(value, bool):
                node[key] = str(value).lower()
            elif value is None:
                node[key] = 'null'
            elif isinstance(value, dict):
                node[key] = inner(value)
            else:
                node[key] = value
        return node
    return inner(file)


def chooseType(file):
    if os.path.splitext(file)[1] == '.json':
        file = boolTolower(json.load(open(file)))
    elif (os.path.splitext(file)[1] == '.yml') or \
         (os.path.splitext(file)[1] == '.yaml'):
        file = open(file)
        file = boolTolower(yaml.load(file, Loader=yaml.FullLoader))
    return file


def find_diff(node1, node2):
    diff = []

    def inner(node1, node2, path=''):
        nonlocal diff
        removed = set(node1) - set(node2)
        added = set(node2) - set(node1)
        others = set(node2) - added
        for key in removed:
            diff.append([key, path + key, node1[key], 'rm'])
        for key in added:
            diff.append([key, path + key, 'rm', node2[key]])
        for key in others:
            diff.append([key, path + key, node1[key], node2[key]])
            path_int = path + key + '.'
            if isinstance(node1[key], dict) and isinstance(node2[key], dict):
                inner(node1[key], node2[key], path=path_int)
    inner(node1, node2)
    return diff


def find_diff1(node1, node2):
    removed, ident, updated, added = set(), set(), set(), set()

    def inner(node1, node2):
        nonlocal removed, ident, updated, added
        removed = removed | (set(node1) - set(node2))
        added = added | (set(node2) - set(node1))
        for key, value in node2.items():
            if key in node1:
                if value == node1[key]:
                    ident.add(key)
                else:
                    updated.add(key)
                if isinstance(value, dict):
                    inner(node1[key], node2[key])
    inner(node1, node2)
    return {'removed': removed,
            'ident': ident,
            'updated': updated,
            'added': added,
            }


def generate_diff(file_path1, file_path2):
    file1 = chooseType(file_path1)
    file2 = chooseType(file_path2)
    diff = find_diff(file1, file2)
    diff = sorted(diff, key=lambda x: x[1])
    return stylish(diff)
