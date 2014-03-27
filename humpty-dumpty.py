__author__ = 'jingyuan'
import math


def checkio(height, width):
    a = width / 2.0
    c = height / 2.0
    if c < a:
        e = (1 - (c / a) ** 2) ** .5
        s = round(2 * math.pi * a ** 2 * (1 + (1 - e ** 2) / e * math.atanh(e)), 2)
    elif c == a:
        s = round(4 * math.pi * a ** 2, 2)
    else:
        e = (1 - (a / c) ** 2) ** .5
        s = round(2 * math.pi * a ** 2 * (1 + c / (a * e) * math.asin(e)), 2)
    v = round((4 * math.pi / 3) * a ** 2 * c, 2)
    return [v, s]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"
