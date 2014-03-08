__author__ = 'jingyuan'


def checkio(expr):
    #replace this for solution
    opn = []
    opn.append('#')
    for c in expr:
        if c in ['(', '[', '{']:
            opn.append(c)
        elif c == ')':
            if opn[-1] == '(':
                opn.pop()
            else:
                return False
        elif c == ']':
            if opn[-1] == '[':
                opn.pop()
            else:
                return False
        elif c == '}':
            if opn[-1] == '{':
                opn.pop()
            else:
                return False
    if opn[-1] == '#':
        return True
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"((5+3)*2+1)") == True, "Simple"
    assert checkio(u"{[(3+1)+2]+}") == True, "Different types"
    assert checkio(u"(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio(u"[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio(u"(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"