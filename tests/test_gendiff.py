from gendiff.generate_diff import generate_diff


def test_gendiff():
    result = generate_diff('tests/fixtures/file_path1.json', 'tests/fixtures/file_path2.json')
    result2 = open('tests/fixtures/result_json.txt')
    final_result = ''
    for elem in result:
        if elem in result2:
            final_result += elem
    assert result == final_result