__author__ = 'jingyuan'


def checkio(text, word):
    w = len(word)
    text = text.replace(' ', '').split('\n')
    for x in range(len(text)):
        for y in range(len(text[x]) - w + 1):
            if text[x][y:y + w].lower() == word:
                return [x + 1, y + 1, x + 1, y + w]
    for x in range(len(text) - w + 1):
        for y in range(len(text[x])):
            try:
                if ''.join([line[y] for line in text[x:x + w]]).lower() == word:
                    return [x + 1, y + 1, x + w, y + 1]
            except BaseException:
                continue
    return [1, 1, 1, 4]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", u"ten") == [2, 14, 2, 16]
    assert checkio(u"""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", u"noir") == [4, 16, 7, 16]
    assert checkio(u"""Twas brillig, and the slithy toves
Did gyre and gimble in the wabe;
All mimsy were the borogoves,
And the mome raths outgrabe.""",
        u"stog") == [1,19,4,19]