from operator import sub

def locate(n):
    """
    Here we use three dimensions (x, y, z) to locate a number.
    The coordinate of 1 is (0, 0, 0).
    The positive direction of x is 1->7.
    The positive direction of y is 7->2.
    The positive direction of z is 2->1.
    """
    l, x, y, z = 0, 0, 0, 0
    # determine the level n belongs
    while 6 * l * (l + 1) / 2 + 1 < n:
        l += 1
        #backtrace
    diff = 6 * l * (l + 1) / 2 + 1 - n
    x = l
    if diff <= l:
        z += diff
        return x, y, z
    diff -= l
    z += l
    if diff <= l:
        x -= diff
        return x, y, z
    diff -= l
    x -= l
    if diff <= l:
        y += diff
        return x, y, z
    diff -= l
    y += l
    if diff <= l:
        z -= diff
        return x, y, z
    diff -= l
    z -= l
    if diff <= l:
        x += diff
        return x, y, z
    diff -= l
    x += l
    y -= diff

    return x, y, z


def distance(a, b):
    """
    This method calculate the distance between two point
    """
    dx, dy, dz = map(sub, a, b)
    #use x, y to represent the distance
    x = dx - dz
    y = dy - dz
    #if x, y has the same sign
    if x * y > 0:
        return abs(x + y) - min(abs(x), abs(y))
    return abs(x) + abs(y)


def hex_spiral(first, second):
    return distance(locate(first), locate(second))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert hex_spiral(2, 9) == 1, "First"
    assert hex_spiral(9, 2) == 1, "Reverse First"
    assert hex_spiral(6, 19) == 2, "Second, short way"
    assert hex_spiral(5, 11) == 3, "Third"
    assert hex_spiral(13, 15) == 2, "Fourth, One row"
    assert hex_spiral(11, 17) == 4, "Fifth, One more test"
