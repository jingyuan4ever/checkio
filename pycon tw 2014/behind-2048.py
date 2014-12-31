win = [['U','W','I','N']]*4
lose = [['G','A','M','E'],['O','V','E','R']]*2


def rotateRight(state):
    return [list(line) for line in zip(*state[::-1])]


def pullLeft(state):
    for i in xrange(0, 4):
        for j in xrange(0, 3):
            if state[i][j] != 0:
                for k in range(j+1, 4):
                    if state[i][k] != 0:
                        break
                if state[i][k] == state[i][j]:
                    state[i][j] *= 2
                    state[i][k] = 0
        for j in xrange(0, 3):
            if state[i][j] == 0:
                for k in range(j+1, 4):
                    if state[i][k] != 0:
                        break
                state[i][j] = state[i][k]
                state[i][k] = 0
    return state


def check(state):
    moved = False
    for i in xrange(3,-1,-1):
        for j in xrange(3,-1,-1):
            if not moved and state[i][j] == 0:
                state[i][j] = 2
                moved = True
            if state[i][j] == 2048:
                return win
    if not moved:
        return lose
    return state

def move2048(state, move):
    if move == 'up':
        state = rotateRight(state)
        state = rotateRight(state)
        state = rotateRight(state)
        state = pullLeft(state)
        state = rotateRight(state)
    elif move == 'down':
        state = rotateRight(state)
        state = pullLeft(state)
        state = rotateRight(state)
        state = rotateRight(state)
        state = rotateRight(state)
    elif move == 'left':
        state = pullLeft(state)
    elif move == 'right':
        state = rotateRight(state)
        state = rotateRight(state)
        state = pullLeft(state)
        state = rotateRight(state)
        state = rotateRight(state)
    else:
        pass
    state = check(state)
    return state


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert move2048([[0, 2, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 2, 0, 0]], 'up') == [[0, 4, 0, 0],
                                              [0, 0, 0, 0],
                                              [0, 0, 0, 0],
                                              [0, 0, 0, 2]], "Start. Move Up!"
    assert move2048([[4, 0, 0, 0],
                     [0, 4, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 8, 8]], 'right') == [[0, 0, 0, 4],
                                                 [0, 0, 0, 4],
                                                 [0, 0, 0, 0],
                                                 [0, 0, 2, 16]], "Simple right"
    assert move2048([[2, 0, 2, 2],
                     [0, 4, 4, 4],
                     [8, 8, 8, 16],
                     [0, 0, 0, 0]], 'right') == [[0, 0, 2, 4],
                                                 [0, 0, 4, 8],
                                                 [0, 8, 16, 16],
                                                 [0, 0, 0, 2]], "Three merging"
    assert move2048([[256, 0, 256, 4],
                     [16, 8, 8, 0],
                     [32, 32, 32, 32],
                     [4, 4, 2, 2]], 'right') == [[0, 0, 512, 4],
                                                 [0, 0, 16, 16],
                                                 [0, 0, 64, 64],
                                                 [0, 2, 8, 4]], "All right"
    assert move2048([[4, 4, 0, 0],
                     [0, 4, 1024, 0],
                     [0, 256, 0, 256],
                     [0, 1024, 1024, 8]], 'down') == [['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N'],
                                                      ['U', 'W', 'I', 'N']], "We are the champions!"
    assert move2048([[2, 4, 8, 16],
                     [32, 64, 128, 256],
                     [512, 1024, 2, 4],
                     [8, 16, 32, 64]], 'left') == [['G', 'A', 'M', 'E'],
                                                   ['O', 'V', 'E', 'R'],
                                                   ['G', 'A', 'M', 'E'],
                                                   ['O', 'V', 'E', 'R']], "Nobody moves!"
