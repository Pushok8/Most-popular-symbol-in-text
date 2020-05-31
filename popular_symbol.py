"""
The popular_symbol module.

This module contains one function for calculating
the most common character in the text. There are a lot of
supported characters (12679 UTF-8 code points starting from zero),
so is it possible to exhaust this list?
"""
from typing import Text, Dict

__all__ = ['max_symbol']
__author = '©Pushok8'
_CHARS = [chr(i) for i in range(12679 + 1)]


def max_symbol(text: Text) -> tuple:
    """
    max_symbol(text: Text) -> tuple:

    Searches for the most frequently occurring character in the text.
    If two characters occur equally often,then the most recent one is returned.
    :param text: The text in which you need to find a frequently occurring character.
    :return: Returns the character and the number of references to it in the text.
    """
    for i in text:
        assert i in _CHARS, 'There is no such symbol in the list.'
    if text == '':
        return 'Your text is incorrect!'

    quantity_letters: Dict[str, int] = {}
    for letter in _CHARS:
        quantity_letters.update({letter: text.count(letter)})

    max_val: int = max(quantity_letters.values())
    print(max_val)
    for letter in _CHARS:
        if quantity_letters[letter] == max_val:
            return letter, max_val
