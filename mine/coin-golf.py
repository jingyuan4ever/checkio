def golf(c):
    l=len(c)+1
    c.sort()
    d=[[1]*l]
    i=0
    while 1:
        i+=1
        d.append([0]*l)
        for j in range(1,l):
            d[i][j]=d[i][j-1]
            if c[j-1]<=i:
                d[i][j]|=d[i-c[j-1]][j-1]
        if not sum(d[i]):
            return i
    return 0


print golf([9, 2, 2, 1]) == 6
print golf([1, 1, 1, 1]) == 5
print golf([1, 2, 3, 4, 5]) == 16