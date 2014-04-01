__author__ = 'jingyuan'
import itertools
import random

candidates = None


def edist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5


def checkio(steps):
    global candidates
    if len(steps) == 1:
        candidates = list(itertools.product(range(10), repeat=2))
        return [0, 0]

    prex, prey = steps[-2][0], steps[-2][1]
    nowx, nowy, dis = steps[-1]
    for x, y in candidates[:]:
        if dis == 0:
            if edist(prex, prey, x, y) != edist(nowx, nowy, x, y):
                candidates.remove((x, y))
        if dis == -1:
            if edist(prex, prey, x, y) >= edist(nowx, nowy, x, y):
                candidates.remove((x, y))
        if dis == 1:
            if edist(prex, prey, x, y) <= edist(nowx, nowy, x, y):
                candidates.remove((x, y))
    ret = random.choice(candidates)
    candidates.remove(ret)
    return list(ret)


if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    from math import hypot

    MAX_STEP = 12

    def check_solution(func, goal, start):
        prev_steps = [start]
        for step in range(MAX_STEP):
            row, col = func([s[:] for s in prev_steps])
            if [row, col] == goal:
                return True
            if 10 <= row or 0 > row or 10 <= col or 0 > col:
                print("You gave wrong coordinates.")
                return False
            prev_distance = hypot(prev_steps[-1][0] - goal[0], prev_steps[-1][1] - goal[1])
            distance = hypot(row - goal[0], col - goal[1])
            alteration = 0 if prev_distance == distance else (1 if prev_distance > distance else -1)
            prev_steps.append([row, col, alteration])
        print("Too many steps")
        return False

    assert check_solution(checkio, [7, 7], [5, 5, 0]), "1st example"
    assert check_solution(checkio, [5, 6], [0, 0, 0]), "2nd example"
