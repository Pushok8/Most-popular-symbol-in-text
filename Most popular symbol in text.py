def getKeyByValue(dic, val, alphabet):
    for letter in alphabet:
        if dic[letter] == val:
            return letter


def mostPopularSymbolInText(text):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', ' ', '!', '.', ',', '?', '_', '-', '+', '=', '>', '<', '/', '\\', '@', '#',
                '0',
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '"', '\'', '|', ')', '(', ':', ';', '`', '~', '*', '&',
                '^', '%', '$', '№']

    for i in text:
        if not i in alphabet:
            return 'Your text is incorrect!'
    if text == '':
        return 'Your text is incorrect!'

    dic = {}
    for letter in alphabet:
        sumSymbolInText = text.count(letter)
        dic.update({letter: sumSymbolInText})
    maxVal = max(dic.values())
    maxKey = getKeyByValue(dic, maxVal, alphabet)
    topSymbol = 'Most popular symbol in this text - ' + str(maxKey) + '. His value - ' + str(maxVal)
    return topSymbol
