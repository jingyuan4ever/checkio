__author__ = 'jingyuan'
import itertools


def checkio(crossword, words):
    crossword2 = zip(*crossword)
    numDict = dict()
    for i in range(5):
        for j in range(5):
            if crossword[i][j] != 0:
                numDict.setdefault(crossword[i][j], 0)
                if i % 2 == 0 and j % 2 == 0:
                    numDict[crossword[i][j]] += 2
                else:
                    numDict[crossword[i][j]] += 1
    wordDict = dict()
    rWordDict = dict()
    for w in words:
        for c in w:
            wordDict.setdefault(c, 0)
            wordDict[c] += 1
    for i in wordDict:
        rWordDict.setdefault(wordDict[i], []).append(i)
    solution = dict()
    for i in range(0, 5, 2):
        cw = itertools.product(rWordDict[numDict[crossword[i][0]]], rWordDict[numDict[crossword[i][1]]],
                               rWordDict[numDict[crossword[i][2]]], rWordDict[numDict[crossword[i][3]]],
                               rWordDict[numDict[crossword[i][4]]])
        for c in cw:
            if ''.join(c) in words:
                for j in range(5):
                    solution[crossword[i][j]] = c[j]
        cw = itertools.product(rWordDict[numDict[crossword2[i][0]]], rWordDict[numDict[crossword2[i][1]]],
                               rWordDict[numDict[crossword2[i][2]]], rWordDict[numDict[crossword2[i][3]]],
                               rWordDict[numDict[crossword2[i][4]]])
        for c in cw:
            if ''.join(c) in words:
                for j in range(5):
                    solution[crossword2[i][j]] = c[j]

    ret = []
    for i in range(5):
        ret.append([])
        for j in range(5):
            if crossword[i][j] == 0:
                ret[i].append(' ')
            else:
                ret[i].append(solution[crossword[i][j]])
    return ret


if __name__ == '__main__':
    assert checkio(
        [
            [21, 6, 25, 25, 17],
            [14, 0, 6, 0, 2],
            [1, 11, 16, 1, 17],
            [11, 0, 16, 0, 5],
            [26, 3, 14, 20, 6]
        ],
        ['hello', 'habit', 'lemma', 'ozone', 'bimbo', 'trace']
    ) == [['h', 'e', 'l', 'l', 'o'],
          ['a', ' ', 'e', ' ', 'z'],
          ['b', 'i', 'm', 'b', 'o'],
          ['i', ' ', 'm', ' ', 'n'],
          ['t', 'r', 'a', 'c', 'e']]
