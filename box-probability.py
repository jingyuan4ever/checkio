__author__ = 'jingyuan'
from fractions import Fraction


def formatFloat(c):
    if int(c) == c:
        return int(c)

    fmt = '%.2f' % c
    if fmt[-1] == '0':
        return float(fmt[:-1])

    return float(fmt)


def checkio(marbles, step):
    parts = [(marbles.count('b'), marbles.count('w'), 1)]
    length = len(marbles)
    for i in range(step - 1):
        newParts = []
        for j in parts:
            b, w, c = j
            if b != 0:
                newParts.append((b - 1, w + 1, Fraction(b, length) * c))
            if w != 0:
                newParts.append((b + 1, w - 1, Fraction(w, length) * c))
        parts = newParts
    ret = 0
    for i in parts:
        b, w, c = i
        ret += Fraction(w, length) * c
    print formatFloat(float(ret))
    return formatFloat(float(ret))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u'bbw', 3) == 0.48, "1st example"
    assert checkio(u'wwb', 3) == 0.52, "2nd example"
    assert checkio(u'www', 3) == 0.56, "3rd example"
    assert checkio(u'bbbb', 1) == 0, "4th example"
    assert checkio(u'wwbb', 4) == 0.5, "5th example"
    assert checkio(u'bwbwbwb', 5) == 0.48, "6th example"
