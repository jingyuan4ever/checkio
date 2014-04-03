__author__ = 'jingyuan'
import itertools


def char2int(c):
    return ord(c) - ord('a') + 1


def checkio(cells):
    """str -> int
    Number of moves in the shortest path of knight
    """
    src, des = cells.split('-')
    src = char2int(src[0]), int(src[1])
    des = char2int(des[0]), int(des[1])
    dirs = list(itertools.product([2, -2], [1, -1]))
    dirs.extend(list(itertools.product([1, -1], [2, -2])))
    opn = []
    closed = []
    status = dict()
    now = src
    status[now] = 0
    while now != des:
        closed.append(now)
        for d in dirs:
            newP = (now[0] + d[0], now[1] + d[1])
            if newP[0] in range(1, 9) and newP[1] in range(1, 9):
                if newP in closed:
                    continue
                if newP in opn:
                    continue
                opn.append(newP)
                status[newP] = status[now] + 1
        now = opn.pop(0)

    return status[now]


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(u"b1-d5") == 2, "1st example"
    assert checkio(u"a6-b8") == 1, "2nd example"
    assert checkio(u"h1-g2") == 4, "3rd example"
    assert checkio(u"h8-d7") == 3, "4th example"
    assert checkio(u"a1-h8") == 6, "5th example"