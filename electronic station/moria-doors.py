import re


def similarity(word1, word2):
    s = 0.0
    if word1[0] == word2[0]:
        s += 0.1
    if word1[-1] == word2[-1]:
        s += 0.1
    if len(word1) > len(word2):
        s += 0.3*len(word2)/len(word1)
    else:
        s += 0.3*len(word1)/len(word2)
    s1 = set(word1)
    s2 = set(word2)
    s += 0.5*len(s1.intersection(s2))/len(s1.union(s2))
    return s


def find_word(message):
    message = [s for s in re.compile(r"\W").split(message.lower()) if s][::-1]
    return max(message, key=lambda i: sum([similarity(i, j) for j in message]))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word(u"Speak friend and enter.") == "friend", "Friend"
    assert find_word(u"Beard and Bread") == "bread", "Bread is Beard"
    assert find_word(u"The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     u"I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word(u"Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     u" According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word(u"One, two, two, three, three, three.") == "three", "Repeating"
