__author__ = 'jingyuan'


def getAction(state):
    ret = []
    if len(state[0]) != 0:
        ret.append('01')
        ret.append('02')
    if len(state[1]) != 0:
        ret.append('12')
        if len(state[0]) == 0:
            ret.append('10')
    if len(state[2]) != 0:
        ret.append('21')
        if len(state[0]) == 0:
            ret.append('20')
    return ret


def act(state, action):
    ret = [x[:] for x in state]
    src = int(action[0])
    dest = int(action[1])
    ret[dest].append(ret[src].pop())
    return ret


def hash(state):
    return '-'.join([''.join(x) for x in state])


def parse(string):
    return [x[::1] for x in string.split('-')]


def checkio(data):
    start, end = data.split("-")
    opn = []
    cls = []
    state = dict()
    now = [[], list(start), []]
    state[hash(now)] = None
    while now != [[], [], list(end)]:
        cls.append(now)
        actions = getAction(now)
        for a in actions:
            nxt = act(now, a)
            if nxt in cls:
                continue
            if nxt in opn:
                continue
            if nxt not in opn:
                opn.append(nxt)
                state[hash(nxt)] = (hash(now), a)
        now = opn.pop(0)
    path = []
    now = hash(now)
    while state[now]:
        s = state[now]
        path.append(s[1])
        now = s[0]
    return ','.join(path[::-1])


if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    GOOD_ACTIONS = ("12", "10", "01", "02", "20", "21")

    def check_solution(func, anagrams, min_length):
        start, end = anagrams.split("-")
        stacks = [[], list(start), []]
        user_result = func(anagrams)
        actions = user_result.split(",")
        user_actions = []
        for act in actions:
            if act not in GOOD_ACTIONS:
                print("Wrong action")
                return False
            from_s = int(act[0])
            to_s = int(act[1])
            if not stacks[from_s]:
                print("You can not get from an empty stack")
                return False
            if to_s == 0 and stacks[to_s]:
                print("You can not push in the full buffer")
                return False
            stacks[to_s].append(stacks[from_s].pop())
            user_actions.append(act)
        res_word = ''.join(stacks[2])
        if len(actions) > min_length:
            print("It can be shorter.")
            return False
        if res_word == end:
            return True
        else:
            print("The result anagram is wrong.")
            return False

    assert check_solution(checkio, u"rice-cire", 5), "rice-cire"
    assert check_solution(checkio, u"tort-trot", 4), "tort-trot"
    assert check_solution(checkio, u"hello-holle", 14), "hello-holle"
    assert check_solution(checkio, u"anagram-mragana", 8), "anagram-mragana"
    assert check_solution(checkio, u"mirror-mirorr", 25), "mirror-mirorr"
