__author__ = 'jingyuan'
from collections import Counter


def merge(tree, src, dest):
    matrixLength = len(tree)
    for x in range(matrixLength):
        for y in range(matrixLength):
            if tree[x][y] == src:
                tree[x][y] = dest


def checkio(matrix):
    matrixLength = len(matrix)
    mergeTree = [[x + y * matrixLength for x in range(matrixLength)] for y in range(matrixLength)]
    for x in range(matrixLength):
        for y in range(matrixLength):
            if x != matrixLength - 1:
                if matrix[x][y] == matrix[x + 1][y] and mergeTree[x + 1][y] != mergeTree[x][y]:
                    merge(mergeTree, mergeTree[x + 1][y], mergeTree[x][y])
            if x != 0:
                if matrix[x][y] == matrix[x - 1][y] and mergeTree[x - 1][y] != mergeTree[x][y]:
                    merge(mergeTree, mergeTree[x - 1][y], mergeTree[x][y])
            if y != matrixLength - 1:
                if matrix[x][y] == matrix[x][y + 1] and mergeTree[x][y + 1] != mergeTree[x][y]:
                    merge(mergeTree, mergeTree[x][y + 1], mergeTree[x][y])
            if y != 0:
                if matrix[x][y] == matrix[x][y - 1] and mergeTree[x][y - 1] != mergeTree[x][y]:
                    merge(mergeTree, mergeTree[x][y - 1], mergeTree[x][y])
    cnt = Counter()
    for x in range(matrixLength):
        for y in range(matrixLength):
            cnt[mergeTree[x][y]] += 1
    index, times = cnt.most_common(1)[0]
    return [times, matrix[index / matrixLength][index % matrixLength]]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [1, 2, 3, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1, 1, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 1, 1, 1]
    ]) == [14, 1], "14 of 1"

    assert checkio([
        [2, 1, 2, 2, 2, 4],
        [2, 5, 2, 2, 2, 2],
        [2, 5, 4, 2, 2, 2],
        [2, 5, 2, 2, 4, 2],
        [2, 4, 2, 2, 2, 2],
        [2, 2, 4, 4, 2, 2]
    ]) == [19, 2], '19 of 2'