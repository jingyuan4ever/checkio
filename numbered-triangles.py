__author__ = 'jingyuan'
import itertools


def check(chips, chip_order, rotation_order):
    total = 0
    for i in range(len(chips)):
        chip = chips[chip_order[i]]
        rotation = rotation_order[i]
        prev_chip = chips[chip_order[i - 1]]
        prev_rotation = rotation_order[i - 1]
        if chip[rotation[0]] != prev_chip[prev_rotation[1]]:
            return 0
        total += chip[rotation[2]]
    return total

def checkio(chips):
    perm = set(r if r[0] < r[-1] else r[::-1] for r in itertools.permutations(range(1, 6), 5))
    chip_orders = [[0] + list(r) for r in perm]

    rotation = itertools.permutations(range(3), 3)
    rotation_orders = list(itertools.product(rotation, repeat=6))

    return max(check(chips, chip_order, rotation_order) for chip_order in chip_orders for rotation_order in rotation_orders)

    #These "asserts" using only for self-checking and not necessary for auto-testing


if __name__ == '__main__':
    assert checkio(
        [[1, 4, 20], [3, 1, 5], [50, 2, 3],
         [5, 2, 7], [7, 5, 20], [4, 7, 50]]) == 152, "First"
    assert checkio(
        [[1, 10, 2], [2, 20, 3], [3, 30, 4],
         [4, 40, 5], [5, 50, 6], [6, 60, 1]]) == 210, "Second"
    assert checkio(
        [[1, 2, 3], [2, 1, 3], [4, 5, 6],
         [6, 5, 4], [5, 1, 2], [6, 4, 3]]) == 21, "Third"
    assert checkio(
        [[5, 9, 5], [9, 6, 9], [6, 7, 6],
         [7, 8, 7], [8, 1, 8], [1, 2, 1]]) == 0, "Fourth"