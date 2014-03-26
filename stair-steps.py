__author__ = 'jingyuan'


def dp(numbers, x, b):
    if x == -1:
        return 0
    if x == 0:
        if b:
            return numbers[0]
        return 0
    if b:
        return max(dp(numbers, x - 1, True), dp(numbers, x - 1, False)) + numbers[x]
    return dp(numbers, x - 1, True)


def checkio(numbers):
    numbers.append(0)
    return dp(numbers, len(numbers) - 1, True)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([5, -3, -1, 2]) == 6, 'Fifth'
    assert checkio([5, 6, -10, -7, 4]) == 8, 'First'
    assert checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95]) == 393, 'Second'
    assert checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27]) == 125, 'Third'
    print('All ok')