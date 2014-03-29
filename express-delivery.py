__author__ = 'jingyuan'
import itertools
from operator import add


def disMap(s, field_map):
    opn = [s]
    closed = []
    nodes = list(itertools.product(range(len(field_map)), range(len(field_map[0]))))
    dis = dict()
    dis[s] = 0
    while opn:
        now = opn.pop(0)
        closed.append(now)
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = tuple(map(add, now, d))
            if neighbor in nodes and field_map[neighbor[0]][neighbor[1]] != 'W':
                if neighbor in closed:
                    continue
                if neighbor in opn:
                    continue
                opn.append(neighbor)
                dis[neighbor] = dis[now] + 1
    return dis


def findPath(s, e, field_map):
    opn = []
    closed = [s]
    nodes = list(itertools.product(range(len(field_map)), range(len(field_map[0]))))
    father = dict()
    father[s] = None
    now = s
    while now != e:
        closed.append(now)
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = tuple(map(add, now, d))
            if neighbor in nodes and field_map[neighbor[0]][neighbor[1]] != 'W':
                if neighbor in closed:
                    continue
                if neighbor in opn:
                    continue
                opn.append(neighbor)
                father[neighbor] = now
        now = opn.pop(0)
    ACTIONS = {
        (0, -1): "L",
        (0, 1): "R",
        (-1, 0): "U",
        (1, 0): "D"
    }

    path = []
    while father[now]:
        pre = father[now]
        path.append(ACTIONS[(now[0]-pre[0], now[1]-pre[1])])
        now = pre
    return ''.join(path[::-1])


def checkio(field_map):
    boxList = []
    for i in range(len(field_map)):
        for j in range(len(field_map[0])):
            if field_map[i][j] == 'S':
                s = (i, j)
            if field_map[i][j] == 'E':
                e = (i, j)
            if field_map[i][j] == 'B':
                boxList.append((i, j))

    disFromStart = disMap(s, field_map)
    disFromEnd = disMap(e, field_map)

    minTime = 2 * disFromStart[e]
    boxes = None

    for b1, b2 in [(x, y) for x in boxList for y in boxList]:
        dis = 2 + 2 * disFromStart[b1]
        dis += 2 * disFromEnd[b2]
        dis += disMap(b1, field_map)[b2]
        if dis < minTime:
            minTime = dis
            boxes = [b1, b2]

    if boxes:
        return findPath(s, boxes[0], field_map)+'B'+findPath(boxes[0], boxes[1], field_map)+'B'+findPath(boxes[1], e, field_map)
    else:
        return findPath(s, e, field_map)


if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    ACTIONS = {
        "L": (0, -1),
        "R": (0, 1),
        "U": (-1, 0),
        "D": (1, 0),
        "B": (0, 0)
    }

    def check_solution(func, max_time, field):
        max_row, max_col = len(field), len(field[0])
        s_row, s_col = 0, 0
        total_time = 0
        hold_box = True
        route = func(field[:])
        for step in route:
            if step not in ACTIONS:
                print("Unknown action {0}".format(step))
                return False
            if step == "B":
                if hold_box:
                    if field[s_row][s_col] == "B":
                        hold_box = False
                        total_time += 1
                        continue
                    else:
                        print("Stephan broke the cargo")
                        return False
                else:
                    if field[s_row][s_col] == "B":
                        hold_box = True
                    total_time += 1
                    continue
            n_row, n_col = s_row + ACTIONS[step][0], s_col + ACTIONS[step][1],
            total_time += 2 if hold_box else 1
            if 0 > n_row or n_row >= max_row or 0 > n_col or n_row >= max_col:
                print("We've lost Stephan.")
                return False
            if field[n_row][n_col] == "W":
                print("Stephan fell in water.")
                return False
            s_row, s_col = n_row, n_col
            if field[s_row][s_col] == "E" and hold_box:
                if total_time <= max_time:
                    return True
                else:
                    print("You can deliver the cargo faster.")
                    return False
        print("The cargo is not delivered")
        return False

    assert check_solution(checkio, 12, ["S...", "....", "B.WB", "..WE"]), "1st Example"
    assert check_solution(checkio, 11, ["S...", "....", "B..B", "..WE"]), "2nd example"