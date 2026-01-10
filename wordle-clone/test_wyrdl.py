# test_wyrdl.py
# Test in the terminal:
# pytest test_wyrdl.py

import wyrdl


def test_get_random_word():
    """Test that a random word from the word list is chosen."""
    word_list = ["CRANE", "SNAKE", "WYRDL"]
    assert wyrdl.get_random_word(word_list) in word_list
