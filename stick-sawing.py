__author__ = 'jingyuan'
def fn(n):
    return n*(n+1)*(n+2)/6

def f(n):
    return n*(n+1)/2

def checkio(number):
    for i in range(44, 0, -1):
        for j in range(1, 46-i):
            if fn(j+i-1)-fn(j-1) == number:
                l = []
                for k in range(i):
                    l.append(f(j+k))
                return l
    return []

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
