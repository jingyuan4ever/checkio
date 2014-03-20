__author__ = 'jingyuan'

DIRS = {"N": -4, "S": 4, "E": 1, "W": -1}


def getRoomDir(house, number):
    room_dir = [ch for ch in "NWES" if ch not in house[number - 1]]
    if number % 4 == 1 and "W" in room_dir:
        room_dir.remove("W")
    if not number % 4 and "E" in room_dir:
        room_dir.remove("E")
    if number <= 4 and "N" in room_dir:
        room_dir.remove("N")
    if number > 12 and "S" in room_dir:
        room_dir.remove("S")
    return room_dir


def getDis(house, start):
    dis = dict()
    dis[start] = 0
    toGo = [start]
    visited = [start]
    while toGo:
        room = toGo.pop(0)
        for my_dir in getRoomDir(house, room):
            nxtRoom = room + DIRS[my_dir]
            if nxtRoom not in visited:
                visited.append(nxtRoom)
                dis[nxtRoom] = dis[room] + 1
                toGo.append(nxtRoom)
    return dis


def checkio(house, stephan, ghost):
    from random import choice

    if stephan == 1:
        return 'N'

    DIRS = {"N": -4, "S": 4, "E": 1, "W": -1}

    disExit = getDis(house, 1)

    disGhost = getDis(house, ghost)
    if disGhost[stephan] > 2:
        my_dirs, my_dist = "", 1000
        for my_dir in getRoomDir(house, stephan):
            if disExit[stephan + DIRS[my_dir]] < my_dist:
                my_dirs, my_dist = my_dir, disExit[stephan + DIRS[my_dir]]
            elif disExit[stephan + DIRS[my_dir]] == my_dist:
                my_dirs += my_dir
        my_dir = choice(my_dirs)

        return my_dir

    my_dirs, my_dist = "", 0
    for my_dir in getRoomDir(house, stephan):
        if disGhost[stephan + DIRS[my_dir]] > my_dist:
            my_dirs, my_dist = my_dir, disGhost[stephan + DIRS[my_dir]]
        elif disGhost[stephan + DIRS[my_dir]] == my_dist:
            my_dirs += my_dir

    dirs = my_dirs

    my_dirs, my_dist = "", 1000
    for my_dir in dirs:
        if disExit[stephan + DIRS[my_dir]] < my_dist:
            my_dirs, my_dist = my_dir, disExit[stephan + DIRS[my_dir]]
        elif disExit[stephan + DIRS[my_dir]] == my_dist:
            my_dirs += my_dir

    my_dirs = [my_dir for my_dir in my_dirs if len(getRoomDir(house, stephan+DIRS[my_dir])) != 1]
    print my_dirs
    my_dir = choice(my_dirs)


    return my_dir


if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    from random import choice

    DIRS = {"N": -4, "S": 4, "E": 1, "W": -1}

    def check_solution(func, house):
        stephan = 16
        ghost = 1
        for step in range(30):
            direction = func(house[:], stephan, ghost)
            if direction in house[stephan - 1]:
                print('Stefan ran into a closed door. It was hurt.')
                return False
            if stephan == 1 and direction == "N":
                print('Stefan has escaped.')
                return True
            stephan += DIRS[direction]
            if ((direction == "W" and stephan % 4 == 0) or (direction == "E" and stephan % 4 == 1) or
                    (stephan < 1) or (stephan > 16)):
                print('Stefan has gone out into the darkness.')
                return False
            sx, sy = (stephan - 1) % 4, (stephan - 1) // 4
            ghost_dirs = [ch for ch in "NWES" if ch not in house[ghost - 1]]
            if ghost % 4 == 1 and "W" in ghost_dirs:
                ghost_dirs.remove("W")
            if not ghost % 4 and "E" in ghost_dirs:
                ghost_dirs.remove("E")
            if ghost <= 4 and "N" in ghost_dirs:
                ghost_dirs.remove("N")
            if ghost > 12 and "S" in ghost_dirs:
                ghost_dirs.remove("S")

            ghost_dir, ghost_dist = "", 1000
            for d in ghost_dirs:
                new_ghost = ghost + DIRS[d]
                gx, gy = (new_ghost - 1) % 4, (new_ghost - 1) // 4
                dist = (gx - sx) ** 2 + (gy - sy) ** 2
                if ghost_dist > dist:
                    ghost_dir, ghost_dist = d, dist
                elif ghost_dist == dist:
                    ghost_dir += d
            ghost_move = choice(ghost_dir)
            ghost += DIRS[ghost_move]
            if ghost == stephan:
                print('The ghost caught Stephan.')
                return False
        print("Too many moves.")
        return False

    assert check_solution(checkio,
                          ["", "S", "S", "",
                           "E", "NW", "NS", "",
                           "E", "WS", "NS", "",
                           "", "N", "N", ""]), "1st example"
    assert check_solution(checkio,
                          ["", "", "", "",
                           "E", "ESW", "ESW", "W",
                           "E", "ENW", "ENW", "W",
                           "", "", "", ""]), "2nd example"
    check_solution(checkio, ["", "", "ES", "W", "E", "W", "N", "", "E", "WS", "S", "", "", "N", "N", ""])
