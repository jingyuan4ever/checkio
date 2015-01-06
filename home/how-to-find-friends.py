def check_connection(network, first, second):
    d = dict()
    for i in network:
        p1, p2 = i.split('-')
        d.setdefault(p1, []).append(p2)
        d.setdefault(p2, []).append(p1)
    opn = [first]
    cls = []
    while len(opn):
        now = opn.pop()
        cls.append(now)
        if now == second:
            return True
        for next in d.setdefault(now, []):
            if next not in cls and next not in opn:
                opn.append(next)
    return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
