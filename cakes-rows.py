__author__ = 'jingyuan'
import itertools

def hashLine(line):
    ls = []
    for l in line:
        ls.append(str(l[0]))
        ls.append(str(l[1]))
    return ''.join(ls)


def isLine(triple):
    c1, c2, c3 = triple
    x1, y1 = c1
    x2, y2 = c2
    x3, y3 = c3
    if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
        return True
    return False


def checkio(cakes):
    lines = [c for c in itertools.combinations(cakes, 3) if isLine(c)]
    d = dict()
    for i, line in enumerate(lines):
        d[hashLine(line)] = i
    for i in range(len(lines)-1):
        for j in range(i, len(lines)):
            s1 = set()
            for k in lines[i]:
                s1.add(tuple(k))
            s2 = set()
            for k in lines[j]:
                s2.add(tuple(k))
            if len(s1.intersection(s2)) == 2:
                m = min(d[hashLine(lines[i])], d[hashLine(lines[j])])
                d[hashLine(lines[i])] = m
                d[hashLine(lines[j])] = m
    n = len(set(d.values()))

    return n

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
        [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
         [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6