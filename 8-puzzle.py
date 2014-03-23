__author__ = 'jingyuan'

MOVES = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

def deepcopy(puzzle):
    return [x[:] for x in puzzle]

def puzzle2int(puzzle):
    ret = ''
    for i in range(3):
        for j in range(3):
            ret += str(puzzle[i][j])
    return int(ret)


class state():
    def __init__(self, puzzle, g, pre):
        self.puzzle = puzzle
        self.h = self._h_()
        self.g = g
        self.pre = pre

    def __hash__(self):
        return puzzle2int(self.puzzle)


    def _h_(self):
        h = 0
        for x, row in enumerate(self.puzzle):
            for y, value in enumerate(row):
                if value != 0:
                    destx = (value - 1) / 3
                    desty = (value - 1) % 3
                    h += abs(x - destx) + abs(y - desty)
        return h

    def __str__(self):
        ret = ''
        for i in range(3):
            for j in range(3):
                ret += str(self.puzzle[i][j])
        return ret

    def isComplete(self):
        return self.h == 0

    def getBlank(self):
        for i in range(3):
            for j in range(3):
                if self.puzzle[i][j] == 0:
                    return i, j

    def nextMove(self):
        ret = []
        i, j = self.getBlank()
        for m in MOVES:
            newi = i + MOVES[m][0]
            newj = j + MOVES[m][1]
            if 0 <= newi < 3 and 0 <= newj < 3:
                newPuzzle = deepcopy(self.puzzle)
                newPuzzle[newi][newj], newPuzzle[i][j] = newPuzzle[i][j], newPuzzle[newi][newj]
                ret.append(newPuzzle)
        return ret

    def f(self):
        return self.g + self.h


def checkio(puzzle):
    now = state(deepcopy(puzzle), 0, None)
    opened = {}
    closed = {}
    opened[hash(now)] = now
    while not now.isComplete():
        opened.pop(hash(now))
        closed[hash(now)] = now
        nxt = now.nextMove()
        for n in nxt:
            if puzzle2int(n) in closed.keys():
                continue
            if puzzle2int(n) not in opened.keys():
                newState = state(n, now.g + 1, now)
                opened[hash(newState)] = newState
            else:
                if opened[puzzle2int(n)].f() > now.f() + 1:
                    opened[puzzle2int(n)].g = now.g + 1
                    opened[puzzle2int(n)].pre = now
        now = min(opened.items(), key=lambda x: x[1].f())[1]
    route = ''
    while now.pre:
        nxt = now
        now = now.pre
        x1, y1 = now.getBlank()
        x2, y2 = nxt.getBlank()
        dx, dy = x2 - x1, y2 - y1
        for m in MOVES:
            if MOVES[m] == (dx, dy):
                route += m
    return route[::-1]


if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    GOAL = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    MOVES = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

    def check_solution(func, puzzle):
        size = len(puzzle)
        route = func([row[:] for row in puzzle])
        goal = GOAL
        x = y = None
        for i, row in enumerate(puzzle):
            if 0 in row:
                x, y = i, row.index(0)
                break
        for ch in route:
            swap_x, swap_y = x + MOVES[ch][0], y + MOVES[ch][1]
            if 0 <= swap_x < size and 0 <= swap_y < size:
                puzzle[x][y], puzzle[swap_x][swap_y] = puzzle[swap_x][swap_y], 0
                x, y = swap_x, swap_y
        if puzzle == goal:
            return True
        else:
            print("Puzzle is not solved")
            return False

    assert check_solution(checkio, [[1, 2, 3],
                                    [4, 6, 8],
                                    [7, 5, 0]]), "1st example"
    assert check_solution(checkio, [[7, 3, 5],
                                    [4, 8, 6],
                                    [1, 2, 0]]), "2nd example"
    assert check_solution(checkio, [[2, 4, 5], [1, 7, 3], [8, 6, 0]]), "2nd example"

