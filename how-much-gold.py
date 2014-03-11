__author__ = 'jingyuan'

from fractions import Fraction

METALS = ('gold', 'tin', 'iron', 'copper')


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


def checkio(alloys):
    """
        Find proportion of gold
    """
    matrix = []
    right = []
    for item in alloys:
        vector = [0 for x in range(4)]
        first, second = item.split('-')
        proportion = alloys[item]
        for (k, i) in enumerate(METALS):
            if i == first or i == second:
                vector[k] = proportion.denominator
        right.append(proportion.numerator)
        matrix.append(vector)
    vector = [1 for x in range(4)]
    matrix.append(vector)
    right.append(1)
    denominator = determinantValue(matrix)

    for i in range(4):
        matrix[i][0] = right[i]
    numerator = determinantValue(matrix)

    return Fraction(numerator, denominator)


# this is a better answer
# def checkio(alloys):
#     """
#         Find proportion of gold
#     """
#     # According to description all test are solvable so let's find other 3 sums
#     for alloy in alloys.copy():
#         alloys['-'.join(set(METALS)-set(alloy.split('-')))] = \
#                 1 - alloys[alloy]
#     # Now just calculate the proportion of gold from all three proportions that
#     # includes 'gold'
#     return (sum([alloys[x] for x in alloys if 'gold' in x]) - 1) / 2


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({
        'gold-tin': Fraction(1, 2),
        'gold-iron': Fraction(1, 3),
        'gold-copper': Fraction(1, 4),
    }) == Fraction(1, 24), "1/24 of gold"
    assert checkio({
        'tin-iron': Fraction(1, 2),
        'iron-copper': Fraction(1, 2),
        'copper-tin': Fraction(1, 2),
    }) == Fraction(1, 4), "quarter"
    assert checkio({
        "iron-tin": Fraction(2, 3),
        "iron-copper": Fraction(1, 4),
        "iron-gold": Fraction(1, 2),
    }) == Fraction(7, 24)
