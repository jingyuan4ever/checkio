def letter_queue(commands):
    l = []
    for c in commands:
        if c.startswith('PUSH'):
            l.append(c[5])
        else:
            if len(l) > 0:
                l.pop(0)
    return ''.join(l)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
