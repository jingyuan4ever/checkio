import re

def translate(phrase):
    pattern = re.compile('(([aeiouy])[aeiouy]{2})|(([^aeiouy])[aeiouy])')
    return ' '.join([''.join([i.group(2) or i.group(4) for i in pattern.finditer(word)]) for word in phrase.split(' ')])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate(u"hieeelalaooo") == "hello", "Hi!"
    assert translate(u"hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate(u"aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate(u"sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
