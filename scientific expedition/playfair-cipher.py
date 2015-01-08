import string
m = "abcdefghijklmnopqrstuvwxyz0123456789"

def getNewArray(key):
    newM = []
    for c in key+m:
        if c not in newM:
            newM.append(c)
    return newM

def getIndex(x, y):
    return 6 * x + y

def getPosition(i):
    return i/6, i%6

def encodeInner(m, first, second):
    x1, y1 = getPosition(m.index(first))
    x2, y2 = getPosition(m.index(second))
    if x1 == x2:
        first = m[getIndex(x1, (y1+1)%6)]
        second = m[getIndex(x2, (y2+1)%6)]
    elif y1 == y2:
        first = m[getIndex((x1+1)%6, y1)]
        second = m[getIndex((x2+1)%6, y2)]
    else:
        first = m[getIndex(x1, y2)]
        second = m[getIndex(x2, y1)]
    return first+second


def encode(message, key):
    message = [string.lower(c) for c in message if c.isalnum()]
    newM = getNewArray(key)
    newMessage = []
    i = 0
    while i!=len(message):
        if i+1 == len(message):
            if message[i] == 'z':
                newMessage.append(encodeInner(newM, 'z', 'x'))
            else:
                newMessage.append(encodeInner(newM, message[i], 'z'))
            i += 1
        elif message[i] == message[i+1]:
            if message[i] == 'x':
                newMessage.append(encodeInner(newM, 'x', 'z'))
            else:
                newMessage.append(encodeInner(newM, message[i], 'x'))
            i += 1
        else:
            newMessage.append(encodeInner(newM, message[i], message[i+1]))
            i += 2
    return ''.join(newMessage)


def decodeInner(m, first, second):
    x1, y1 = getPosition(m.index(first))
    x2, y2 = getPosition(m.index(second))
    if x1 == x2:
        first = m[getIndex(x1, (y1-1)%6)]
        second = m[getIndex(x2, (y2-1)%6)]
    elif y1 == y2:
        first = m[getIndex((x1-1)%6, y1)]
        second = m[getIndex((x2-1)%6, y2)]
    else:
        first = m[getIndex(x1, y2)]
        second = m[getIndex(x2, y1)]
    return first+second


def decode(secret_message, key):
    newM = getNewArray(key)
    newMessage = []
    for i in range(0, len(secret_message), 2):
        newMessage.append(decodeInner(newM, secret_message[i], secret_message[i+1]))
    return ''.join(newMessage)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert encode("Fizz Buzz is x89 XX.", "checkio101") == 'do2y7mt22kry94y2y2', "Encode fizz buzz"
    assert decode("do2y7mt22kry94y2y2", "checkio101") == 'fizxzbuzzisx89xzxz', "Decode fizz buzz"
    assert encode("How are you?", "hello") == 'ea2imb1ht0', "Encode How are you"
    assert decode("ea2imb1ht0", "hello") == 'howareyouz', "Decode How are you"
    assert encode("My name is Alex!!!", "alexander") == 'i1dlkxjqlexn', "Encode Alex"
    assert decode("i1dlkxjqlexn", "alexander") == 'mynameisalex', "Decode Alex"
    assert encode("Who are you?", "human") == 'rnvftc1jd5', "Encode WHo"
    assert decode("rnvftc1jd5", "human") == 'whoareyouz', "Decode Who"
    assert encode("ATTACK AT DAWN", "general") == 'ewwektewhnua', "Encode attack"
    assert decode("ewwektewhnua", "general") == 'attackatdawn', "Decode attack"
