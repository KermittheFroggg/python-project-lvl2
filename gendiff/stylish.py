import itertools


def stylish_help(elem, depth_new):
    ident = ' '
    res_str = ''
    ident_new = ident * (depth_new * 4 + 2)
    if isinstance(elem[2], dict) and isinstance(elem[3], dict):
        res_str += f'{ident_new}  {elem[0]}' + ': {\n'
    elif elem[2] == elem[3]:
        res_str += f'{ident_new}  {elem[0]}: {elem[3]}\n'
    elif elem[3] == 'rm':
        res_str += f'{ident_new}- {elem[0]}: ' + (
                   stringify(elem[2], gref=(depth_new + 1) * 2) + '\n')
    elif elem[2] == 'add':
        res_str += f'{ident_new}+ {elem[0]}: ' + (
                   stringify(elem[3], gref=(depth_new + 1) * 2) + '\n')
    else:
        res_str += f'{ident_new}- {elem[0]}: ' + (
                   stringify(elem[2], gref=(depth_new + 1) * 2) + '\n')
        res_str += f'{ident_new}+ {elem[0]}: ' + (
                   stringify(elem[3], gref=(depth_new + 1) * 2) + '\n')
    return res_str


def stylish(diff):
    ident = ''
    res_str = ''
    depth_new = 0
    depth_old = 0
    for index, elem in enumerate(diff):
        depth_new = elem[1].count('.')
        if depth_new < depth_old:
            for i in range(-depth_old, -depth_new):
                res_str += ident * ((-i) * 4) + '}' + '\n'
        res_str += stylish_help(elem, depth_new)
        if index == (len(diff) - 1) and depth_new > 0:
            res_str += ident * depth_new * 4 + '}'
        depth_old = depth_new
    return '{\n' + res_str + '}'


def stringify(value, replacer='  ', spaces_count=2, gref=1):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, gref)
