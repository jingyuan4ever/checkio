def guide(pawns):
    row, col = pawns[0], pawns[1]
    g1 = chr(ord(row)-1)+chr(ord(col)-1)
    g2 = chr(ord(row)+1)+chr(ord(col)-1)
    return [g1, g2]

def safe_pawns(pawns):
    c = 0
    for i in pawns:
        for g in guide(i):
            if g in pawns:
                c+=1
                break
    return c


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
