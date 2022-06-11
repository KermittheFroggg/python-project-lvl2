def plain(diff):
    result = ''
    for elem in diff:
        if 'rm' in elem:
            result += 'Property ' + modernize(elem[1]) + ' was removed' + '\n'
        elif 'add' in elem:
            result += 'Property ' + modernize(elem[1]) + \
                ' was added with value: ' + modernize(elem[3]) + '\n'
        else:
            if not (isinstance(elem[2], dict) and (
                    isinstance(elem[3], dict))) and (
                    elem[2] != elem[3]):
                result += 'Property ' + modernize(elem[1]) + \
                    " was updated. From " + \
                    modernize(elem[2]) + ' to ' + modernize(elem[3]) + '\n'
    return result.strip('\n')


def modernize(elem):
    if isinstance(elem, dict):
        return '[complex value]'
    else:
        if elem not in ('true', 'false', 'null'):
            return f"'{elem}'"
        elif isinstance(elem, int):
            return f"'{elem}'"
        else:
            return elem
