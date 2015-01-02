def r(a,b):
    if type(b)==int:
        a.append(b)
        return a
    return reduce(r,b,a)

def flat_list(a):
    return reduce(r,a,[])


print flat_list([1, 2, 3]) == [1, 2, 3]
print flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
print flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
print flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]