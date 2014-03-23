__author__ = 'jingyuan'


def checkio(number):
    ret = 1
    for c in str(number):
        if int(c) != 0:
            ret *= int(c)

    return ret

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
