__author__ = 'jingyuan'
import operator


def checkio(first, second):
    ops = [operator.or_, operator.and_, operator.xor]
    ret = 0
    for i in bin(first)[2:]:
        for op in ops:
            ret += int(''.join([str(op(int(i), int(x))) for x in bin(second)[2:]]), 2)
    return ret

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18