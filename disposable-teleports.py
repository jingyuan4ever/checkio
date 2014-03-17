__author__ = 'jingyuan'


def checkio(teleports_string):
    route = ['1']
    portals = dict()
    for i in teleports_string.split(','):
        portals.setdefault(i[0], []).append(i[1])
        portals.setdefault(i[1], []).append(i[0])
    pre = 0
    while len(set(route)) != len(portals) or route[-1] != '1':
        current = route[-1]
        open = [x for x in portals[current] if x > pre]
        if not open:
            route.pop(-1)
            pre = current
            portals[pre].append(route[-1])
            portals[route[-1]].append(pre)

        else:
            m = min(open)
            route.append(m)
            portals[m].remove(current)
            portals[current].remove(m)
            pre = 0
    return ''.join(route)

#This part is using only for self-testing
if __name__ == "__main__":
    def check_solution(func, teleports_str):
        route = func(teleports_str)
        teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_str.split(",")]
        if route[0] != '1' or route[-1] != '1':
            print("The path must start and end at 1")
            return False
        ch_route = route[0]
        for i in range(len(route) - 1):
            teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
            if not teleport in teleports_map:
                print("No way from {0} to {1}".format(route[i], route[i + 1]))
                return False
            teleports_map.remove(teleport)
            ch_route += route[i + 1]
        for s in range(1, 9):
            if not str(s) in ch_route:
                print("You forgot about {0}".format(s))
                return False
        return True

    assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
    assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
    assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
    assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"