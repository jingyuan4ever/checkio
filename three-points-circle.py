__author__ = 'jingyuan'


def isInt(x):
    return float(round(x)) == x


def checkio(data):
    """
    assume two points are p0(x0,y0), p1(x1,y1)
    the middle point is (mx, my) = ((x0+x1)/2, (y0+y1)/2)
    the slope k is dy/dx = (y1-y0)/(x1-x0)
    so the slope of midperpendicular is -dx/dy
    midperpendicular function is dy*(y-my)+dx*(x-mx)=0
    i.e. y = (dy*my-dx*x+dx*mx)/dy
    so we got two midperpendicular functions
    y = (dy01*my01-dx01*x+dx01*mx01)/dy01
    y = (dy02*my02-dx02*x+dx02*mx02)/dy02
    then we can calculate the center of circle as
    x = (dx01*dy02*mx01+dx01*dx02*my01-dx02*dy01*my02-dx02*dy01*mx02)/(-dx02*dy01+dx01*dy02)
    """
    (x0, y0), (x1, y1), (x2, y2) = eval(data)
    dx01, dy01 = x0 - x1, y0 - y1
    dx02, dy02 = x0 - x2, y0 - y2
    mx01, my01 = (x0 + x1) / 2.0, (y0 + y1) / 2.0
    mx02, my02 = (x0 + x2) / 2.0, (y0 + y2) / 2.0
    x = (dy01 * dy02 * my01 + dx01 * dy02 * mx01 - dy02 * dy01 * my02 - dx02 * dy01 * mx02) / (
        - dx02 * dy01 + dx01 * dy02)
    y = 0
    if dy01 != 0:
        y = (dy01 * my01 - dx01 * x + dx01 * mx01) / dy01
    elif dy02 != 0:
        y = (dy02 * my02 - dx02 * x + dx02 * mx02) / dy02
    else:
        print "can not build a circle"
    r = ((x - x0) ** 2 + (y - y0) ** 2) ** 0.5
    print x, y, r
    ret = ""
    if isInt(x):
        ret += "(x-%d)^2+" % round(x)
    else:
        ret += "(x-%.3g)^2+" % x
    if isInt(y):
        ret += "(y-%d)^2=" % round(y)
    else:
        ret += "(y-%.3g)^2=" % y
    if isInt(r):
        ret += "%d^2" % round(r)
    else:
        ret += "%.3g^2" % r
    return ret

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"(2,2),(6,2),(2,6)") == "(x-4)^2+(y-4)^2=2.83^2"
    assert checkio(u"(3,7),(6,9),(9,7)") == "(x-6)^2+(y-5.75)^2=3.25^2"
