def g(a,b,c,d,e,f,n):
    if n==0:
        return a
    if n==1:
        return b
    if n==2 and c!=0:
        return c
    s=d*g(a,b,c,d,e,f,n-1)+e*g(a,b,c,d,e,f,n-2)
    if f!=0:
        s+=f*g(a,b,c,d,e,f,n-3)
    return s

def fibgolf(t,n):
    if t==u'fibonacci':
        return g(0,1,0,1,1,0,n)
    if t==u'tribonacci':
        return g(0,1,1,1,1,1,n)
    if t==u'lucas':
        return g(2,1,0,1,1,0,n)
    if t==u'jacobsthal':
        return g(0,1,0,1,2,0,n)
    if t==u'pell':
        return g(0,1,0,2,1,0,n)
    if t==u'perrin':
        return g(3,0,2,0,1,1,n)
    if t==u'padovan':
        return g(0,1,1,0,1,1,n)
    return 0


if __name__ == '__main__':
    assert fibgolf(u'fibonacci', 10) == 55
    assert fibgolf(u'tribonacci', 10) == 149
    assert fibgolf(u'lucas', 10) == 123
    assert fibgolf(u'jacobsthal', 10) == 341
    assert fibgolf(u'pell', 10) == 2378
    assert fibgolf(u'perrin', 10) == 17
    assert fibgolf(u'padovan', 10) == 9

