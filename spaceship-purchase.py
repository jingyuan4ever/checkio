__author__ = 'jingyuan'

def checkio(data):

    a, b, c, d = data
    if a >= c:
        return c
    while a < c:
        a+=b
        if a >= c:
            return c
        c-=d
        if c <= a:
            return a



#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([150, 50, 1000, 100]) == 450, "1st example"
    assert checkio([150, 50, 900, 100]) == 400, "2nd example"
