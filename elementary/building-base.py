class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.__s = south
        self.__w = west
        self.__wwe = width_WE
        self.__wns = width_NS
        self.__h = height
        self.__c = {}

    def corners(self):
        self.__c['north-east'] = [self.__s+self.__wns, self.__w+self.__wwe]
        self.__c['south-east'] = [self.__s, self.__w+self.__wwe]
        self.__c['south-west'] = [self.__s, self.__w]
        self.__c['north-west'] = [self.__s+self.__wns, self.__w]
        return self.__c

    def area(self):
        return self.__wwe*self.__wns

    def volume(self):
        return self.__wwe*self.__wns*self.__h

    def __repr__(self):
        return "Building(%r, %r, %r, %r, %r)" % (self.__s, self.__w, self.__wwe, self.__wns, self.__h)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
