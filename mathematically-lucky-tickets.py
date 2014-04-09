__author__ = 'jingyuan'
import operator
from fractions import Fraction

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.div
}.items()


def checkio(ticket):
    subresults = {}

    def calculate(start, end):
        p = (start, end)
        if p not in subresults:
            n = ticket[start:end + 1]
            sr = subresults[p] = {int(n): n}
            for s in xrange(start, end):
                for op_name, op_func in OPERATORS:
                    for r1, e1 in calculate(start, s).items():
                        for r2, e2 in calculate(s + 1, end).items():
                            try:
                                res = op_func(Fraction(r1), Fraction(r2))
                            except ZeroDivisionError:
                                continue
                            if res not in sr:
                                sr[res] = '(%s %s %s)' % (e1, op_name, e2)
        return subresults[p]

    results = calculate(0, len(ticket) - 1)
    if 100 in results:
        return False
    else:
        return True

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u'000000') == True, "All zeros"
    assert checkio(u'707409') == True, "You can not transform it to 100"
    assert checkio(u'595347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
    assert checkio(u'271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"
    assert checkio(u"100478") == True
    assert checkio(u"836403") == False
