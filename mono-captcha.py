__author__ = 'jingyuan'
FONT = [[0,1,1,0,0,0,1,0,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,0,1,1,0,1,1,1,0,1,1,1,0,0,1,1,0],
        [0,1,0,1,0,1,1,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0],
        [0,1,0,1,0,0,1,0,0,0,1,1,0,0,1,0,0,1,1,1,0,1,1,0,0,1,1,1,0,0,1,0,0,1,1,1,0,1,1,1,0],
        [0,1,0,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0],
        [0,0,1,1,0,0,1,0,0,1,1,1,0,1,1,1,0,0,0,1,0,1,1,0,0,0,1,1,0,1,0,0,0,1,1,1,0,1,1,0,0]]

def getNum(n):
    return [line[4*n+1:4*n+4] for line in FONT]


def diff(image, font):
    count = 0
    for i in range(5):
        for j in range(3):
            if image[i][j] != font[i][j]:
                count+=1
    return count




def checkio(image):
    n = len(image[0])/4
    ret = []
    for i in range(n):
        num = [line[4*i+1:4*i+4] for line in image]
        diffDict = dict()
        for i in range(10):
            diffDict[i] = diff(num, getNum(i))
        ret.append(sorted(diffDict.items(), key=lambda x:x[1])[0][0])
    return int(''.join([str(x) for x in ret]))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "394 clear"
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "again 394 but with noise"
