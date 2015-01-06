import fractions


def divide_pie(groups):
    n = sum([abs(x) for x in groups])
    remain = fractions.Fraction(1, 1)
    for i in groups:
        if i > 0:
            remain -= fractions.Fraction(i, n)
        else:
            remain *= 1 - fractions.Fraction(abs(i), n)
    if remain < 0:
        remain = 0
    return remain.numerator, remain.denominator

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"
