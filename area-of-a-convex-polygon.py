__author__ = 'jingyuan'
def areaOfTriangleDot(d1, d2, d3):
    return areaOfTriangleVector((d2[0]-d1[0], d2[1]-d1[1]), (d3[0]-d1[0], d3[1]-d1[1]))


def areaOfTriangleVector(e1, e2):
    return abs((e1[1]*e2[0]-e2[1]*e1[0])/2.0)


def checkio(data):
    basePoint = [data.pop(0)]
    length = len(data)
    ret = sum(map(areaOfTriangleDot, basePoint*(length-1), data[:length-1], data[1:length]))
    return ret

if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio([[1, 1], [9, 9], [9, 1]]), 32), "The half of the square"
    assert almost_equal(checkio([[4, 10], [7, 1], [1, 4]]), 22.5), "Triangle"
    assert almost_equal(checkio([[1, 2], [3, 8], [9, 8], [7, 1]]), 40), "Quadrilateral"
    assert almost_equal(checkio([[3, 3], [2, 7], [5, 9], [8, 7], [7, 3]]), 26), "Pentagon"
    assert almost_equal(checkio([[7, 2], [3, 2], [1, 5], [3, 9], [7, 9], [9, 6]]), 42), "Hexagon"
    assert almost_equal(checkio([[4, 1], [3, 4], [3, 7], [4, 8], [7, 9], [9, 6], [7, 1]]), 35.5), "Heptagon"
