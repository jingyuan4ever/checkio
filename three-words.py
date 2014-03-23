__author__ = 'jingyuan'
def checkio(words):
    count = 0
    for word in words.split(' '):
        if word[0].isdigit():
            count = 0
        else:
            count += 1
        if count == 3:
            return True
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Hello World hello") == True, "Hello"
    assert checkio(u"He is 123 man") == False, "123 man"
    assert checkio(u"1 2 3 4") == False, "Digits"
    assert checkio(u"bla bla bla bla") == True, "Bla Bla"
    assert checkio(u"Hi") == False, "Hi"
