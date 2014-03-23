__author__ = 'jingyuan'


class position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = 20 - self.x - self.y
        self.h = self.x + self.y - 2

    def setFrom(self, p):
        self.frm = p
        self.h = p.getH() + 1

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getG(self):
        return self.g

    def getH(self):
        return self.h

    def getF(self):
        return self.g + self.h


class maze:
    def __init__(self, data):
        self.data = data
        self.o = []
        self.c = []
        self.pos = []
        for i in range(0, 12):
            self.pos.append([])
        for i in range(0, 12):
            for j in range(0, 12):
                self.pos[i].append(position(i, j))

    def do(self, p, f):
        if self.data[p.getX()][p.getY()] == 0 and p not in self.c:
            if p not in self.o:
                self.o.append(p)
                p.setFrom(f)
            else:
                if f.getH() + 1 < p.getH():
                    p.setFrom(f)

    def nextStep(self):
        f = 10000
        ret = None
        for p in self.o:
            if p.f() <= f:
                ret = p
        self.o.remove(ret)
        return ret

    def backTrace(self):
        ls = []
        p = self.pos[10][10]
        while p != self.pos[1][1]:
            p, post = p.frm, p
            if p.getX() - post.getX() == 1:
                ls.append('N')
            elif p.getX() - post.getX() == -1:
                ls.append('S')
            elif p.getY() - post.getY() == 1:
                ls.append('W')
            else:
                ls.append('E')
        return ls

    def walk(self):
        p = self.pos[1][1]
        while p.getX() != 10 or p.getY() != 10:
            self.c.append(p)
            north = self.pos[p.getX()][p.getY() - 1]
            self.do(north, p)
            south = self.pos[p.getX()][p.getY() + 1]
            self.do(south, p)
            west = self.pos[p.getX() - 1][p.getY()]
            self.do(west, p)
            east = self.pos[p.getX() + 1][p.getY()]
            self.do(east, p)
            p = self.nextStep()
        return ''.join(self.backTrace()[-1::-1])


def checkio(data):
    m = maze(data)
    return m.walk()

    #Some hints
    #Look to graph search algorithms
    #Don't confuse these with tree search algorithms


    #This code using only for self-checking and not necessary for auto-testing


def checkio2(labyrinth):
    sX, sY = 1, 1
    eX, eY = 10, 10
    paths = [(sX, sY, '')]
    visited = [(sX, sY)]
    while len(paths):
        x, y, p = paths.pop(0)
        if x == eX and y == eY:
            return p
        for i, j, s in [(x + 1, y, 'S'), (x - 1, y, 'N'), (x, y + 1, 'E'), (x, y - 1, 'W')]:
            if labyrinth[i][j] != 1 and (i, j) not in visited: # the borders are always 1
                visited.append((i, j))
                paths.append((i, j, p + s))


if __name__ == '__main__':
    print(checkio2([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))
    #be careful with infinity loop
    print(checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]))
    print(checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]))
    print(checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]))