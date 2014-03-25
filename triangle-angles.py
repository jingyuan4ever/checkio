__author__ = 'jingyuan'
from math import acos
from math import pi


def checkio(a, b, c):
    edges = [a, b, c]
    edges.sort()
    if edges[0] + edges[1] <= edges[2]:
        return [0, 0, 0]
    ang1 = round(acos((edges[1] ** 2 + edges[2] ** 2 - edges[0] ** 2) / float(2 * edges[1] * edges[2]))/pi*180)
    ang2 = round(acos((edges[0] ** 2 + edges[2] ** 2 - edges[1] ** 2) / float(2 * edges[0] * edges[2]))/pi*180)
    ang3 = 180 - ang1 - ang2

    #replace this for solution
    return [ang1, ang2, ang3]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
