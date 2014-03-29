__author__ = 'jingyuan'


def getEdges(start, width):
    ret = []
    for i in range(width):
        ret.append([start + i, start + i + 1])
        ret.append([start + 4 * width + i, start + 4 * width + i + 1])
        ret.append([start + 4 * i, start + 4 * i + 4])
        ret.append([start + width + 4 * i, start + width + 4 * i + 4])
    return ret


def checkio(lines_list):
    """Return the quantity of squares"""
    for l in lines_list:
        if l[0] > l[1]:
            l[0], l[1] = l[1], l[0]
    count = 0
    for width in range(1, 4):
        for i in range(4 - width):
            for j in range((4 - width)):
                isIn = True
                edges = getEdges(4 * i + j + 1, width)
                for e in edges:
                    if e not in lines_list:
                        isIn = False
                        break
                if isIn:
                    count += 1
    return count


if __name__ == '__main__':
    # assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
    #                  [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
    #                  [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    # assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
    #                  [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
    #                  [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    # assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    # assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    # assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
    #                  [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"
    assert (
    checkio([[16, 15], [16, 12], [15, 11], [11, 12], [11, 10], [10, 14], [9, 10], [14, 13], [13, 9], [15, 14]]) == 3)