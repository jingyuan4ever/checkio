__author__ = 'jingyuan'

from fractions import Fraction


def canPass(x1, x2, y1, y2, bunker):
    dx = x1 - x2
    dy = y1 - y2

    if dx == 0:
        if y1 > y2:
            y1, y2 = y2, y1
        for c in bunker[x1][y1:y2 + 1]:
            if c == 'W':
                return False
        return True

    if dy == 0:
        if x1 > x2:
            x1, x2 = x2, x1
        for c in bunker[x1:x2 + 1]:
            if c[y1] == 'W':
                return False
        return True

    k = Fraction((x1 - x2), (y1 - y2))
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            if bunker[i][j] == 'W':
                return False
    return True


def distance(x, y):
    x1, y1 = x
    x2, y2 = y
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5


def checkio(bunker):
    width = len(bunker)
    length = len(bunker[0])
    bats = []
    dest = (0, 0)
    neighbor = {}
    for i in range(width):
        for j in range(length):
            if bunker[i][j] == 'B':
                bats.append((i, j))
            if bunker[i][j] == 'A':
                bats.append((i, j))
                dest = (i, j)
    batsNum = len(bats)
    for i in range(batsNum - 1):
        for j in range(i + 1, batsNum):
            x1, y1 = bats[i]
            x2, y2 = bats[j]
            if canPass(x1, x2, y1, y2, bunker):
                neighbor.setdefault(bats[i], []).append(bats[j])
                neighbor.setdefault(bats[j], []).append(bats[i])
    active = (0, 0)
    open = [active]
    closed = []
    status = {}
    status[active] = (0, distance(active, dest), None)
    while active != dest:
        open.remove(active)
        closed.append(active)
        nxt = neighbor[active]
        for n in nxt:
            if n in closed:
                continue
            if n not in open:
                open.append(n)
                status[n] = (status[active][0] + distance(n, active), distance(n, dest), active)
            else:
                disg = status[active][0] + distance(n, active)
                if status[n][0] > disg:
                    status[n][0] = disg
                    status[n][2] = active
        f = 10000
        for i in open:
            if status[i][0] + status[i][1] < f:
                f = status[i][0] + status[i][1]
                active = i
    now = active
    while status[now][2]:
        print now
        now = status[now][2]

    return status[active][0] + status[active][1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    # assert almost_equal(checkio([
    #     "B--",
    #     "---",
    #     "--A"]), 2.83), "1st example"
    # assert almost_equal(checkio([
    #     "B-B",
    #     "BW-",
    #     "-BA"]), 4), "2nd example"
    # assert almost_equal(checkio([
    #     "BWB--B",
    #     "-W-WW-",
    #     "B-BWAB"]), 12), "3rd example"
    # assert almost_equal(checkio([
    #     "B---B-",
    #     "-WWW-B",
    #     "-WA--B",
    #     "-W-B--",
    #     "-WWW-B",
    #     "B-BWB-"]), 9.24), "4th example"
    #
    # assert almost_equal(checkio(["B-B-B", "-WWW-", "BWA-B", "-WWW-", "B-B-B"]), 8), "5th example"
    assert almost_equal(checkio(["BWA-B-", "-W----", "-WW-B-", "-W---B", "--B---", "B-B---"]), 12.83), "6th example"
