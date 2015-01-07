def digit_stack(commands):
    sum = 0
    q = []
    for command in commands:
        if command.startswith('PUSH'):
            q.append(int(command.split(' ')[1]))
        elif command.startswith('POP'):
            try:
                sum += q.pop()
            except IndexError:
                pass
        else:
            try:
                sum += q[-1]
            except IndexError:
                pass
    return sum

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
