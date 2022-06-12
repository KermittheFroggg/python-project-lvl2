from gendiff.generate_diff import generate_diff


def test_gendiff_format_json():
    result_func = generate_diff('tests/fixtures/filepath1.json', 'tests/fixtures/filepath2.json', format='json').split('\n')
    result_text = open('tests/fixtures/result_format_json.txt', 'r')
    result_text_corr = set()
    for line in result_text:
        result_text_corr.add(line.strip('\n'))
    final_result = set()
    for elem in result_func:
        final_result.add(elem)
    assert result_text_corr == final_result
