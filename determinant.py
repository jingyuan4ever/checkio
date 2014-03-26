__author__ = 'jingyuan'
def determinantValue(matrix):
    """
        calculate the value of determinant
    """

    matrixLength = len(matrix)
    if matrixLength == 1:
        return matrix[0][0]

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

def checkio(data):
    return determinantValue(data)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[4, 3], [6, 3]]) == -6, 'First example'

    assert checkio([[1, 3, 2],
                    [1, 1, 4],
                    [2, 2, 1]]) == 14, 'Second example'
