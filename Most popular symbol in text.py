# Creator: ©Pushok8.
# Date: 25 March 2020.
# Edit 10 April 2020.
# Added documentation and other characters became available.

CHARS = []
for i in range(12679 + 1):
    CHARS.append(chr(i))


def get_key_by_value(dic, val, CHARS):
    for letter in CHARS:
        if dic[letter] == val:
            return letter


def top_symb(text):
    '''
    top_sumb(text)

    Searches for the most frequently occurring character in the text.
    If two characters occur equally often,then the most recent one is returned.
    :param text: The text in which you need to find a frequently occurring character.
    :return:     Returns the character and the number of references to it in the text.
    '''

    for i in text:
        assert i in CHARS, 'There is no such symbol in the list.'
    if text == '':
        return 'Your text is incorrect!'

    quantity_letters = {}

    for letter in CHARS:
        sumSymbolInText = text.count(letter)
        quantity_letters.update({letter: sumSymbolInText})

    maxVal = max(quantity_letters.values())
    maxKey = get_key_by_value(quantity_letters, maxVal, CHARS)
    return (maxKey, maxVal)
