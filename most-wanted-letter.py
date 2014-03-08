__author__ = 'jingyuan'

import re
from collections import Counter

def checkio(text):
    print re.findall("\w", text.lower())
    text = "".join(re.findall("\w", text.lower()))
    print text
    return Counter(text).most_common()[0][0]


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Hello World!") == "l", "Hello test"
    assert checkio(u"How do you do?") == "o", "O is most wanted"
    assert checkio(u"One") == "e", "All letter only once."

