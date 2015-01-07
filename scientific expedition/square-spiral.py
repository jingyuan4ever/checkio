from operator import sub
def position(id):
    i, x, y = 0, 0, 0
    while (2*i+1)**2 < id:
        i += 1
    x -= i
    y += i
    diff = (2*i+1)**2 - id
    if diff > 2*i:
        diff -= 2*i
        y -= 2*i
    else:
        y -= diff
        diff -= diff
    if diff > 2*i:
        diff -= 2*i
        x += 2*i
    else:
        x += diff
        diff -= diff
    if diff > 2*i:
        diff -= 2*i
        y += 2*i
    else:
        y += diff
        diff -= diff
    x -= diff
    return x, y


def find_distance(first, second):
    return sum(map(abs, map(sub, position(first), position(second))))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_distance(1, 9) == 2, "First"
    assert find_distance(9, 1) == 2, "Reverse First"
    assert find_distance(10, 25) == 1, "Neighbours"
    assert find_distance(5, 9) == 4, "Diagonal"
    assert find_distance(26, 31) == 5, "One row"
    assert find_distance(50, 16) == 10, "One more test"