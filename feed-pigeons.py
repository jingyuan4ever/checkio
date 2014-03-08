__author__ = 'jingyuan'


def checkio(n):
    total = 0
    for i in range(1, 10):
        pigeons = sum(range(1, i + 1))
        total += pigeons
        if total >= n:
            return max(sum(range(1, i)), pigeons - total + n)
    return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"