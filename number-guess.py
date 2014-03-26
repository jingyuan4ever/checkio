__author__ = 'jingyuan'
shots = [3, 5, 7]


def checkio(attempts):
    times = len(attempts)
    if times < 4:
        return [shots[times - 1], 1]
    n = 70 * attempts[1][0] + 21 * attempts[2][0] + 15 * attempts[3][0]
    while n > 100:
        n -= 105
    return [2, n]


if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    MAX_ATTEMPT = 8

    def initial_referee(data):
        data["attempt_count"] = 0
        data["guess"] = 0
        return data

    def check_solution(func, goal, initial):
        prev_steps = [initial]
        for attempt in range(MAX_ATTEMPT):
            divisor, guess = func(prev_steps[:])
            if guess == goal:
                return True
            if divisor <= 1 or divisor > 10:
                print("You gave wrong divisor range.")
                return False
            if guess < 1 or guess > 100:
                print("You gave wrong guess number range.")
                return False
            prev_steps.append((goal % divisor, divisor))
        print("Too many attempts.")
        return False

    assert check_solution(checkio, 47, (2, 5)), "1st example"
    assert check_solution(checkio, 94, (3, 7)), "1st example"
    assert check_solution(checkio, 52, (0, 2)), "1st example"
