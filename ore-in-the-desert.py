__author__ = 'jingyuan'
import itertools
import random

candidates = None

def checkio(previous):
    global candidates
    times = len(previous)
    if times == 0:
        candidates = list(itertools.product(range(10), repeat=2))
        candidates.remove((0, 0))
        return [0, 0]

    p = previous[-1]
    remove = []
    for d in candidates:
        if round(((d[0] - p[0]) ** 2 + (d[1] - p[1]) ** 2) ** .5) != p[2]:
            remove.append(d)
    for r in remove:
        candidates.remove(r)
    c = random.choice(candidates)
    return c


if __name__ == '__main__':
    #This part is using only for self-testing.
    def check_solution(func, ore):
        recent_data = []
        for step in range(4):
            row, col = func([d[:] for d in recent_data])  # copy the list
            if row < 0 or row > 9 or col < 0 or col > 9:
                print("Where is our probe?")
                return False
            if (row, col) == ore:
                return True
            dist = round(((row - ore[0]) ** 2 + (col - ore[1]) ** 2) ** 0.5)
            recent_data.append([row, col, dist])
        print("It was the last probe.")
        return False

    assert check_solution(checkio, (1, 1)), "Example"
    assert check_solution(checkio, (9, 9)), "Bottom right"
    assert check_solution(checkio, (6, 6)), "Center"
