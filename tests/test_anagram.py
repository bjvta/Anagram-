"""Test Anagram Module"""

from lib.anagram import check_anagram


def test_anagram_one_true():
    one_word = 'race'
    two_word = 'care'
    assert check_anagram(one_word, two_word)


def test_anagram_two_true():
    one_word = 'part'
    two_word = 'trap'
    assert check_anagram(one_word, two_word)


def test_anagram_three_true():
    one_word = 'Earth'
    two_word = 'heart'
    assert check_anagram(one_word, two_word)


def test_anagram_four_true():
    one_word = 'Knee'
    two_word = 'keen'
    assert check_anagram(one_word, two_word)


def test_anagram_one_false():
    one_word = 'absdf'
    two_word = 'absdd'
    assert check_anagram(one_word, two_word) == False


def test_anagram_two_false():
    one_word = 'qwerqwer'
    two_word = 'rewewrq'
    assert check_anagram(one_word, two_word) == False