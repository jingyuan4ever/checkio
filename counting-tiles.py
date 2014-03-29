__author__ = 'jingyuan'
from math import ceil

def checkio(radius):
    """count tiles"""
    solid, partial = 0, 0
    top = radius
    bottom = radius
    for i in range(1, int(radius)+1):
        bottom = (radius**2-i**2)**.5
        solid += int(bottom)
        partial += int(ceil(top))-int(bottom)
        top = bottom
    if int(radius) != radius:
        partial += int(ceil(bottom))
    return [4*solid, 4*partial]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(2) == [4, 12], "N=2"
    assert checkio(3) == [16, 20], "N=3"
    assert checkio(2.1) == [4, 20], "N=2.1"
    assert checkio(2.5) == [12, 20], "N=2.5"
