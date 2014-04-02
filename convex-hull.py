__author__ = 'jingyuan'


def cmp(d1, d2):
    if d1[0] > d2[0]:
        return 1
    if d1[0] < d2[0]:
        return -1
    if d1[1] > d2[1]:
        return 1
    if d1[1] < d2[1]:
        return -1
    return 0


def checkio(dots):
    """list[list[int, int],] -> list[int,]
    Find the convex hull.
    """
    data = sorted(dots, cmp=cmp)
    basePoint = data.pop(0)
    ret = [basePoint]
    vx = (0, 1)
    dotProduct = []
    for d in data:
        vector = (d[0] - basePoint[0], d[1] - basePoint[1])
        dotProduct.append(
            (round((vx[0] * vector[0] + vx[1] * vector[1]) / (vector[0] ** 2 + vector[1] ** 2) ** .5, 2), d))
    dotProduct.sort(key=lambda x: x[0], reverse=True)
    last = dotProduct[-1][0]
    for i in dotProduct[::-1]:
        if i[0] != last:
            break
    data = dotProduct[:dotProduct.index(i)+1]
    data.extend(dotProduct[:dotProduct.index(i):-1])
    data = [i[1] for i in data]
    ret.append(data.pop(0))
    for d in data:
        while len(ret) > 1:
            p = ret[-1]
            p2 = ret[-2]
            v1 = p2[0] - p[0], p2[1] - p[1]
            v2 = p[0] - d[0], p[1] - d[1]
            if v1[0] * v2[1] - v1[1] * v2[0] > 0:
                ret.pop(-1)
            else:
                break
        ret.append(d)

    return [dots.index(r) for r in ret]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert checkio(
    #     [[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]
    # ) == [4, 5, 6, 0, 1, 2, 3], "First example"
    # assert checkio(
    #     [[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]
    # ) == [1, 0, 6, 3, 5, 2], "Second example"
    # assert checkio([[7, 4], [5, 2], [4, 7], [4, 1], [3, 6], [1, 4]]) == [5, 4, 2, 0, 1, 3]
    assert checkio([[2,6],[5,5],[4,4],[2,2]]) == [3, 0, 1, 2]