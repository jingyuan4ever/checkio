__author__ = 'jingyuan'


def checkio(data):
    syms = set()
    rulesSmaller = {}
    for word in data:
        for sym in word:
            syms.add(sym)

    for sym in syms:
        rulesSmaller.setdefault(sym, set())

    for word in data:
        for i in range(len(word) - 1):
            if word[i] != word[i + 1]:
                rulesSmaller[word[i + 1]].add(word[i])

    parts = []
    for sym in syms:
        if len(rulesSmaller[sym]) == 0:
            parts.append(sym)

    visited = []
    while len(visited) != len(syms):
        while len(parts) != 0:
            now = min(parts)
            visited.append(now)
            parts.remove(now)

            for i in rulesSmaller:
                if now in rulesSmaller[i]:
                    rulesSmaller[i].remove(now)
        for i in [x for x in syms if x not in visited]:
            if len(rulesSmaller[i]) == 0:
                parts.append(i)

    return ''.join(visited)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd",\
        "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm",\
        "Paste in"
    assert checkio(["a", "b", "c"]) == "abc",\
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs",\
        "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg",\
        "Concatenate and paste in"
    assert checkio(["hello", "low", "lino", "itttnosw"]) == "helitnosw"

