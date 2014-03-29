__author__ = 'jingyuan'

def checkio(capacity, number):
    if number <= capacity:
        return ','.join([''.join('0123456789'[:number])]*2)
    s = '0123456789'[:number]*2
    return ','.join([s[i:i+capacity] for i in range(0, number*2, capacity)])


if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    def check_solution(func, k, n, max_steps):
        result = func(k, n)
        actions = result.split(",")
        if len(actions) > max_steps:
            print("It can be shorter.")
            return False
        details = [0] * n
        for act in actions:
            if len(act) > k:
                print("The system can contain {0} detail(s).".format(k))
                return False
            if len(set(act)) < len(act):
                print("You can not place one detail twice in one load")
                return False
            for ch in act:
                details[int(ch)] += 1
        if any(d < 2 for d in details):
            print("I see no painted details.")
            return False
        if any(d > 2 for d in details):
            print("I see over painted details.")
            return False
        return True

    assert check_solution(checkio, 2, 3, 3), "1st Example"
    assert check_solution(checkio, 6, 3, 2), "2nd Example"
    assert check_solution(checkio, 3, 6, 4), "3rd Example"
    assert check_solution(checkio, 1, 4, 8), "4th Example"
    assert check_solution(checkio, 2, 5, 5), "5th Example"
