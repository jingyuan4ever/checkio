__author__ = 'jingyuan'

def checkio(data):
    ret = []
    #replace this for solution
    def traverse(data):
        for d in data:
            if isinstance(d, list):
                traverse(d)
            else:
                ret.append(d)

    traverse(data)
    return ret


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3]) == [1, 2, 3], 'First example'
    assert checkio([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], 'Second example'
    assert checkio([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) ==\
        [2, 4, 5, 6, 6, 6, 6, 6, 7], 'Third example'
