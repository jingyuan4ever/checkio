__author__ = 'jingyuan'


class polynomial:
    """class for polynomial"""


    def __init__(self, expr):
        if isinstance(expr, dict):
            self.dic = expr
            return

        self.dic = dict()
        if expr == 'x':
            self.dic[1] = 1
        else:
            self.dic[0] = int(expr)

    def __add__(self, other):
        # print "add", self, other
        ret = polynomial(self.dic.copy())
        if isinstance(other, int):
            ret.dic.setdefault(0, 0)
            ret.dic[0] += other
            return ret

        for j in other.dic:
            ret.dic.setdefault(j, 0)
            ret.dic[j] += other.dic[j]
        return ret

    def __sub__(self, other):
        # print "sub", self, other
        ret = polynomial(self.dic.copy())
        if isinstance(other, int):
            ret.dic.setdefault(0, 0)
            ret.dic[0] -= other
            return ret

        for j in other.dic:
            ret.dic.setdefault(j, 0)
            ret.dic[j] -= other.dic[j]
        return ret

    def __mul__(self, other):
        # print "mul", self, other
        ret = polynomial(self.dic.copy())
        if isinstance(other, int):
            for i in ret.dic:
                ret.dic[i] *= other
            return ret

        ret = dict()
        for i in self.dic:
            for j in other.dic:
                ret.setdefault(i + j, 0)
                ret[i + j] += self.dic[i] * other.dic[j]
        return polynomial(ret)

    def __neg__(self):
        ret = polynomial(self.dic.copy())
        for i in ret:
            ret[i] = -ret[i]
        return ret

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return -self.__add__(other)

    def __rmul__(self, other):
        # print "mul", self, other
        return self.__mul__(other)


    def __str__(self):
        ret = ''
        for k in self.dic.keys()[::-1]:
            C = self.dic[k]
            if C == 0:
                continue
            elif C == 1:
                if k == 0:
                    ret += '+1'
                else:
                    ret += '+x' + '*x' * (k - 1)
            elif C == -1:
                if k == 0:
                    ret += '-1'
                else:
                    ret += '-x' + '*x' * (k - 1)
            else:
                ret += '%+d' % C
                ret += '*x' * k
        return ret.strip('+')


def checkio(expr):
    # expr = "x-x+"+expr
    ret = eval("x-x+" + expr, {'x': polynomial('x')})
    return str(ret)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio(u"(x-1)*(x+1)") == "x*x-1", "First and simple"
    assert checkio(u"(x+1)*(x+1)") == "x*x+2*x+1", "Almost the same"
    assert checkio(u"(x+3)*x*2-x*x") == "x*x+6*x", "Different operations"
    assert checkio(u"x+x*x+x*x*x") == "x*x*x+x*x+x", "Don't forget about order"
    assert checkio(u"(2*x+3)*2-x+x*x*x*x") == "x*x*x*x+3*x+6", "All together"