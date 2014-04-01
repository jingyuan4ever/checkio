__author__ = 'jingyuan'


def checkio(first, second, goal):
#replace this for solution
    actions = {
        "01": lambda f, s: (first, s),
        "02": lambda f, s: (f, second),
        "12": lambda f, s: (
            f - (second - s if f > second - s else f),
            second if f > second - s else s + f),
        "21": lambda f, s: (
            first if s > first - f else s + f,
            s - (first - f if s > first - f else s),
        ),
        "10": lambda f, s: (0, s),
        "20": lambda f, s: (f, 0)
    }
    f, s = 0, 0
    opn = []
    closed = []
    father = dict()
    now = (f, s)
    father[now] = None
    while now[0] != goal and now[1] != goal:
        closed.append(now)
        for k in actions.keys():
            f, s = actions[k](now[0], now[1])
            if (f, s) in closed:
                continue
            if (f, s) in opn:
                continue
            opn.append((f, s))
            father[(f, s)] = (now, k)
        now = opn.pop(0)

    ret = []
    while father[now]:
        ret.append(father[now][1])
        now = father[now][0]
    return ret[::-1]

if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    def check_solution(func, initial_data, max_steps):
        first_volume, second_volume, goal = initial_data
        actions = {
            "01": lambda f, s: (first_volume, s),
            "02": lambda f, s: (f, second_volume),
            "12": lambda f, s: (
                f - (second_volume - s if f > second_volume - s else f),
                second_volume if f > second_volume - s else s + f),
            "21": lambda f, s: (
                first_volume if s > first_volume - f else s + f,
                s - (first_volume - f if s > first_volume - f else s),
            ),
            "10": lambda f, s: (0, s),
            "20": lambda f, s: (f, 0)
        }
        first, second = 0, 0
        result = func(*initial_data)
        if len(result) > max_steps:
            print("You answer contains too many steps. It can be shorter.")
            return False
        for act in result:
            if act not in actions.keys():
                print("I don't know this action {0}".format(act))
                return False
            first, second = actions[act](first, second)
        if goal == first or goal == second:
            return True
        print("You did not reach the goal.")
        return False

    assert check_solution(checkio, (5, 7, 6), 10), "Example"
    assert check_solution(checkio, (3, 4, 1), 2), "One and two"
