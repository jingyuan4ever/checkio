__author__ = 'jingyuan'
from operator import add

def checkio(data):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    width = len(data)
    height = len(data[0])

    k = 0
    opn = [(0, j) for j in range(height) if data[0][j] == 0]
    dig = [(0, j) for j in range(height) if data[0][j] == 1]
    cls = []
    while True:
        while opn:
            now = opn.pop(0)
            cls.append(now)
            if now[0] == width - 1:
                return k
            for d in dirs:
                nxt = tuple(map(add, now, d))
                if nxt[0] in range(0, width) and nxt[1] in range(0, height):
                    if nxt in cls:
                        continue
                    if nxt in opn:
                        continue
                    if data[nxt[0]][nxt[1]] == 0:
                        opn.append(nxt)
                    else:
                        dig.append(nxt)
        k += 1
        opn = dig
        dig = []

    return 0


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[1, 1, 1, 1, 0, 1, 1],
                    [1, 1, 1, 1, 0, 0, 1],
                    [1, 1, 1, 1, 1, 0, 1],
                    [1, 1, 0, 1, 1, 0, 1],
                    [1, 1, 0, 1, 1, 1, 1],
                    [1, 0, 0, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1, 1]]) == 2, "1st example"
    assert checkio([[0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 0, 1, 0, 1, 1],
                    [1, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0]]) == 3, "2nd example"
    assert checkio([[1, 1, 1, 1, 1, 0, 1, 1],
                    [1, 0, 1, 1, 1, 0, 1, 1],
                    [1, 0, 1, 0, 1, 0, 1, 0],
                    [1, 0, 1, 1, 1, 0, 1, 1],
                    [0, 0, 1, 1, 0, 0, 0, 0],
                    [1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 0, 1, 1, 1, 1]]) == 2, "3rd example"
    assert checkio(
        [[0, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 0, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0, 0]]) == 0