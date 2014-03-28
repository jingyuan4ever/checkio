__author__ = 'jingyuan'

from operator import sub
import sys


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


def fun(a, b):
    return distance(locate(a), locate(b))


def main():
    line = sys.stdin.readline()
    a, b = line.split(' ')
    a = int(a)
    b = int(b)
    sys.stdout.write(str(fun(a, b)))


if __name__ == '__main__':
    main()
