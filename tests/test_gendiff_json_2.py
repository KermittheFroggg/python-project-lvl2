from gendiff.generate_diff import generate_diff


def test_gendiff_stylish():
    result_func = generate_diff('tests/fixtures/filepath1.json', 'tests/fixtures/filepath2.json').split('\n')
    result_text = open('tests/fixtures/result_json_2.txt', 'r')
    result_text_corr = set()
    for line in result_text:
        result_text_corr.add(line.strip('\n'))
    final_result = set()
    for elem in result_func:
        final_result.add(elem)
    assert result_text_corr == final_result
