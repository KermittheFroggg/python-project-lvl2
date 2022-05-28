import json

def generate_diff(file_path1, file_path2, format=json):
    a = json.load(open(file_path1))
    b = json.load(open(file_path2))
    dif_keys_a = set(a) - set(b)
    dif_keys_b = set(b) - set(a)
    same_keys = set(a) & set(b)
    source_a = ''
    source_b = ''
    source_c = ''
    for i in dif_keys_a:
        source_a = source_a + "\n" + ' - ' + str(i) + ': ' + str(a[i])
    for i in same_keys:
        if a[i] == b[i]:
            source_a = source_a + "\n" + '   ' + str(i) + ': ' + str(a[i])
        else:
            source_c = "\n" + ' - ' + str(i) + ': ' + str(a[i]) + "\n" + ' + ' + str(i) + ': ' + str(b[i])
    for i in dif_keys_b:
        source_b = source_b + "\n" + ' + ' + str(i) + ': ' + str(b[i])
    result_a = '{' + source_a 
    result_b = source_b + "\n" + '}'
    result = result_a + source_c + result_b
    return result
