__author__ = 'jingyuan'
import itertools
from fractions import Fraction


def checkio(data):
    ops = itertools.product("01234", repeat=5)
    seqs = itertools.permutations("01234")

    # for op in ops:
    #     for seq in seqs:


    #replace this for solution
    return True or False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u'000000') == True, "All zeros"
    assert checkio(u'707409') == True, "You can not transform it to 100"
    assert checkio(u'595347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
    assert checkio(u'271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"
