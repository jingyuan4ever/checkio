__author__ = 'jingyuan'
import itertools

def getAround(x, y, width, length):
    px = [x+i for i in range(-1, 2) if x+i in range(0, width)]
    py = [y+i for i in range(-1, 2) if y+i in range(0, length)]
    return list(itertools.product(px, py))


def checkio(data):
    width = len(data)
    length = len(data[0])
    unvisited = [(x, y) for x in range(width) for y in range(length)]
    islands = []
    while unvisited:
        x, y = unvisited.pop(0)
        if data[x][y]:
            count = 1
            toGo = getAround(x, y, width, length)
            while toGo:
                i = toGo.pop(0)
                if i in unvisited:
                    unvisited.remove(i)
                    if data[i[0]][i[1]]:
                        count += 1
                        toGo.extend(getAround(i[0], i[1], width, length))
            islands.append(count)
    islands.sort()
    return islands

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
