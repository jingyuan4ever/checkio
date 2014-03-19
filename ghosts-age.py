__author__ = 'jingyuan'


def checkio(opacity):
    if opacity == 10000:
        return 0
    if opacity == 9999:
        return 1

    dx = 10002 - opacity
    now = 1
    nxt = 2
    for i in range(2, 20):
        now, nxt = nxt, now + nxt
        print i, now
        if nxt + i >= dx:
            return now + nxt + i - dx
    return 0

    #These "asserts" using only for self-checking and not necessary for auto-testing


if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"