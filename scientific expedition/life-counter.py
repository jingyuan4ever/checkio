def life_counter(state, tick_n):
    lives = set()
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 1:
                lives.add((i, j))
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(tick_n):
        die = set()
        born = set()
        nei = set()
        for p in lives:
            nei.update([((p[0]+n[0]), (p[1]+n[1])) for n in neighbors])
            if sum([1 for n in neighbors if ((p[0]+n[0]), (p[1]+n[1])) in lives]) not in [2, 3]:
                die.add(p)
        for p in nei:
            if p not in lives and sum([1 for n in neighbors if ((p[0]+n[0]), (p[1]+n[1])) in lives]) == 3:
                born.add(p)
        lives.difference_update(die)
        lives.update(born)

    return len(lives)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print life_counter(((0, 1, 0), (0, 0, 1), (1, 1, 1)), 999)
    assert life_counter(((0, 1, 0, 0, 0, 0, 0),
                         (0, 0, 1, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0)), 4) == 15, "Example"
    assert life_counter(((0, 1, 0, 0, 0, 0, 0),
                         (0, 0, 1, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 1, 1),
                         (0, 0, 0, 0, 0, 0, 0),
                         (1, 1, 1, 0, 0, 0, 0)), 15) == 14, "Little later"
    assert life_counter(((0, 1, 0),
                         (0, 0, 1),
                         (1, 1, 1)), 50) == 5, "Glider"
    assert life_counter(((1, 1, 0, 1, 1),
                         (1, 1, 0, 1, 1),
                         (0, 0, 0, 0, 0),
                         (1, 1, 0, 1, 1),
                         (1, 1, 0, 1, 1)), 100) == 16, "Stones"
