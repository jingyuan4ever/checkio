__author__ = 'jingyuan'


def f(i, j, data):
    if i == 0:
        if data[0] <= j:
            return data[0]
        return 0
    if data[i] > j:
        return f(i - 1, j, data)
    return max(f(i - 1, j, data), f(i - 1, j - data[i], data) + data[i])


def checkio(data):
    total = sum(data)
    data.sort()
    length = len(data)
    n = f(length - 1, total / 2, data)
    return total - 2 * n


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"
    assert checkio([43, 14, 19, 24, 23, 16, 46]) == 1
