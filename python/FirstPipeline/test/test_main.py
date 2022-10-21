from main import select_anagrams, check_anagram

words = ['Anna', 'Ball', 'Hund', 'otto']

def test_select_anagrams():
    expected = ['Anna', 'otto']
    actual = select_anagrams(words)

    assert actual == expected


def test_check_anagram():
    expected_list = [True, False, False, True]

    for word, expected in zip(words, expected_list):
        assert check_anagram(word) == expected


test_select_anagrams()
test_check_anagram()