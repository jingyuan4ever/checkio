class Friends:
    def __init__(self, connections):
        self.__friends = list(connections)

    def add(self, connection):
        if connection in self.__friends:
            return False
        self.__friends.append(connection)
        return True

    def remove(self, connection):
        try:
            self.__friends.remove(connection)
            return True
        except ValueError:
            return False

    def names(self):
        return reduce(set.union, self.__friends)

    def connected(self, name):
        s = reduce(set.union, [f for f in self.__friends if name in f], set())
        s.discard(name)
        return s



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
    print letter_friends.connected("a")
