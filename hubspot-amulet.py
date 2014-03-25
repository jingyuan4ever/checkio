__author__ = 'jingyuan'
from copy import deepcopy
from itertools import product
from math import ceil


def determinantValue(matrix):
    """
        calculate the value of determinant
    """

    matrixLength = len(matrix)
    if matrixLength == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    value = 0
    for i in range(matrixLength):
        sign = 1
        if i % 2 == 1:
            sign = -1
        subMatrix = []
        for j in range(1, matrixLength):
            subMatrix.append(matrix[j][0:i] + matrix[j][i + 1:])
        value += sign * determinantValue(subMatrix) * matrix[0][i]
    return value


def checkio(matrix):
    matrix = [[matrix[j][i] for j in range(3)] for i in range(3)]
    d = determinantValue(matrix)
    n = int(ceil(max([sum(line) for line in matrix])/2.0))
    for c in product(range(-n, n+1), repeat=3):
        ret = []
        for i in range(3):
            m = deepcopy(matrix)
            m[0][i] = 0 + c[0] * 360
            m[1][i] = 225 + c[1] * 360
            m[2][i] = 315 + c[2] * 360
            d2 = determinantValue(m)
            if d2 % d != 0 or -180 > d2 / d or d2 / d > 180:
                break
            ret.append(d2 / d)
        if len(ret) == 3:
            return ret
    return [0, 0, 0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':

    def check_it(func, matrix):
        result = func(matrix)
        if not all(-180 <= el <= 180 for el in result):
            print("The angles must be in range from -180 to 180 inclusively.")
            return False
        f, s, t = result
        temp = [0, 0, 0]
        temp[0] += f
        temp[1] += matrix[0][1] * f
        temp[2] += matrix[0][2] * f

        temp[0] += matrix[1][0] * s
        temp[1] += s
        temp[2] += matrix[1][2] * s

        temp[0] += matrix[2][0] * t
        temp[1] += matrix[2][1] * t
        temp[2] += t
        temp = [n % 360 for n in temp]
        if temp == [0, 225, 315]:
            return True
        else:
            print("This is the wrong final position {0}.".format(temp))
            return False

    assert check_it(checkio,
                    [[1, 2, 3],
                     [3, 1, 2],
                     [2, 3, 1]]), "1st example"
    assert check_it(checkio,
                    [[1, 4, 2],
                     [2, 1, 2],
                     [2, 2, 1]]), "2nd example"
    assert check_it(checkio,
                    [[1, 2, 5],
                     [2, 1, 1],
                     [2, 5, 1]]), "3rd example"