__author__ = 'jingyuan'


def position(data):
    if data == 1:
        return 0, 0
    for i in range(1, 10, 2):
        if data <= i ** 2:
            break
    data -= (i - 2) ** 2 + 1
    n = i / 2
    d, r = data / (i-1), data % (i-1)
    if d == 0:
        return -n + r + 1, n
    if d == 1:
        return n, n - r - 1
    if d == 2:
        return n - r - 1, -n
    if d == 3:
        return -n, -n + r + 1
    return 0, 0


def checkio(data):
    a, b = data
    x1, y1 = position(a)
    x2, y2 = position(b)

    return abs(x1 - x2) + abs(y1 - y2)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 9]) == 2, "First"
    assert checkio([9, 1]) == 2, "Reverse First"
    assert checkio([10, 25]) == 1, "Neighbours"
    assert checkio([5, 9]) == 4, "Diagonal"
    assert checkio([26, 31]) == 5, "One row"
    assert checkio([50, 16]) == 10, "One more test"