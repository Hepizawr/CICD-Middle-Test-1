import pytest
from main import read_file, choose_lines_with_word, write_to_file


@pytest.mark.parametrize("need_word, lines_amount",
                         (
                                 ["Mary", 4],
                                 ["Aleksa", 3],
                         ))
def test_choose_lines_with_word(file_fixture, need_word, lines_amount):
    assert len(choose_lines_with_word(read_file(file_fixture), need_word)) == lines_amount



