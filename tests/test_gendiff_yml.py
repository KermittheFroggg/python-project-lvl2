from gendiff.generate_diff import generate_diff

def test_gendiff():
    result_func = generate_diff('tests/fixtures/file_path1.yml', 'tests/fixtures/file_path2.yml').split('\n')
    result_text = open('tests/fixtures/result_yml.txt', 'r')
    result_text_corr = []
    for line in result_text:
        result_text_corr.append(line.strip('\n'))
    final_result = []
    for elem in result_func:
        if elem in result_text_corr:
            final_result.append(elem)
    assert result_func == final_result