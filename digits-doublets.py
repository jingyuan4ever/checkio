__author__ = 'jingyuan'

def editDistance(a, b):
    a = str(a)
    b = str(b)
    ret = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            ret += 1
    return ret


def checkio(numbers):
    start = numbers[0]
    end = numbers[-1]
    closed = []
    status = dict()
    now = start
    status[now] = -1
    opn = [now]
    while now != end:
        opn.remove(now)
        closed.append(now)
        neighbors = [x for x in numbers if editDistance(now, x) == 1]
        for n in neighbors:
            if n in closed:
                continue
            if n not in opn:
                opn.append(n)
                status[n] = now
        now = opn[0]
    l = []
    while status[now] != -1:
        l.insert(0, now)
        now = status[now]
    l.insert(0, now)
    return l

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"


