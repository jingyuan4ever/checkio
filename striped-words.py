__author__ = 'jingyuan'
import re

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    count = 0
    words = re.split('\W+', text)
    pattern = '^[' + VOWELS + ']?([' + CONSONANTS + '][' + VOWELS + '])*[' + CONSONANTS + ']?$'
    for word in [word for word in words if len(word) != 0 and len(word) != 1]:
        if re.match(pattern, word, re.I):
            count += 1
    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"My name is ...") == 3, "All words are striped"
    assert checkio(u"Hello world") == 0, "No one"
    assert checkio(u"A quantity of striped words.") == 1, "Only of"
    assert checkio(u"Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
