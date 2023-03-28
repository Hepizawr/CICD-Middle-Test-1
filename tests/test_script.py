import pytest

from main import read_file, choose_lines_with_word, write_to_file


@pytest.mark.parametrize("need_word, lines_amount",
                         (
                                 ["Mary", 4],
                                 ["Aleksa", 3],
                         ))
def test_amount_of_choose_lines_with_word(file_fixture, need_word, lines_amount):
    assert len(choose_lines_with_word(read_file(file_fixture), need_word)) == lines_amount


@pytest.mark.parametrize("need_word, expected_lines",
                         (
                                 ["Mary",
                                  ['2 Mary 30.00$ food',
                                   '3 Mary 40.00$ toys',
                                   '6 Mary 70.00$ accessories',
                                   '10 Mary 100.00$ accessories']],
                                 ["Aleksa",
                                  [
                                      '4 Aleksa 50.00$ drinks',
                                      '5 Aleksa 60.00$ accessories',
                                      '9 Aleksa 60.00 Accessories',
                                  ]],
                         ))
def test_choose_lines_with_word(file_fixture, need_word, expected_lines):
    lines = choose_lines_with_word(read_file(file_fixture), need_word)
    chosen_lines = []
    for line in lines:
        for word in line.split(" "):
            if need_word == word:
                chosen_lines.append(line)
                continue
    assert set(chosen_lines) == set(expected_lines)
