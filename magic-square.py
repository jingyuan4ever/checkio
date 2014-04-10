__author__ = 'jingyuan'
# import itertools
#
#
# def test(data):
#     n = len(data)
#     magic_constant = n * (n ** 2 + 1) / 2
#     for i in range(n):
#         if sum(data[i]) != magic_constant:
#             return False
#     trans = zip(*data)
#     for i in range(n):
#         if sum(trans[i]) != magic_constant:
#             return False
#     if sum([data[i][i] for i in range(n)]) != magic_constant:
#         return False
#     if sum([data[i][n-1-i] for i in range(n)]) != magic_constant:
#         return False
#     return True
#
#
# def checkio(data):
#     n = len(data)
#     data2 = [[x for x in y] for y in data]
#     candidates = range(1, n ** 2 + 1)
#     for x in data:
#         for y in x:
#             if y != 0:
#                 candidates.remove(y)
#     for p in itertools.permutations(candidates):
#         k = 0
#         for x in range(n):
#             for y in range(n):
#                 if data[x][y] == 0:
#                     data2[x][y] = p[k]
#                     k += 1
#         if test(data2):
#             return data2
#     return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def is_valid(data):
    n = len(data)
    rows = [sum(row) for row in data]
    cols = [sum(col) for col in zip(*data)]
    diag = [
        sum(data[i][i] for i in range(n)),
        sum(data[i][n-i-1] for i in range(n)),
    ]
    return set(rows + cols + diag) == set([n * (n * n + 1) / 2])

def should_continue(data):
    n = len(data)
    M = n * (n * n + 1) / 2
    return all(sum(row) <= M for row in data) and \
            all(sum(col) <= M for col in zip(*data)) and \
            sum(data[i][i] for i in range(n)) <= M and \
            sum(data[i][n-i-1] for i in range(n)) <= M

def get_candidate(data):
    n = len(data)
    ni, nj = None, None
    for i in range(n):
        for j in range(n):
            if data[i][j] == 0:
                ni, nj = i, j
                break
        if ni is not None: break
    return [(ni, nj, x) for x in set(range(1, n * n + 1)) - set(sum(data, [])) - set([0])]

def backtrack(data):
    if not should_continue(data):
        return None
    if is_valid(data):
        return data
    candidate = get_candidate(data)
    for i, j, c in candidate:
        data[i][j] = c
        r = backtrack(data)
        if r is not None:
            return r
        data[i][j] = 0

def checkio(data):
    return backtrack(data)


if __name__ == '__main__':
    #This part is using only for self-testing.
    def check_solution(func, in_square):
        SIZE_ERROR = "Wrong size of the answer."
        MS_ERROR = "It's not a magic square."
        NORMAL_MS_ERROR = "It's not a normal magic square."
        NOT_BASED_ERROR = "Hm, this square is not based on given template."
        result = func(in_square)
        #check sizes
        N = len(result)
        if len(result) == N:
            for row in result:
                if len(row) != N:
                    print(SIZE_ERROR)
                    return False
        else:
            print(SIZE_ERROR)
            return False
            #check is it a magic square
        # line_sum = (N * (N ** 2 + 1)) / 2
        line_sum = sum(result[0])
        for row in result:
            if sum(row) != line_sum:
                print(MS_ERROR)
                return False
        for col in zip(*result):
            if sum(col) != line_sum:
                print(MS_ERROR)
                return False
        if sum([result[i][i] for i in range(N)]) != line_sum:
            print(MS_ERROR)
            return False
        if sum([result[i][N - i - 1] for i in range(N)]) != line_sum:
            print(MS_ERROR)
            return False

        #check is it normal ms
        good_set = set(range(1, N ** 2 + 1))
        user_set = set([result[i][j] for i in range(N) for j in range(N)])
        if good_set != user_set:
            print(NORMAL_MS_ERROR)
            return False
            #check it is the square based on input
        for i in range(N):
            for j in range(N):
                if in_square[i][j] and in_square[i][j] != result[i][j]:
                    print(NOT_BASED_ERROR)
                    return False
        return True


    assert check_solution(checkio,
                          [[2, 7, 6],
                           [9, 5, 1],
                           [4, 3, 0]]), "1st example"

    assert check_solution(checkio,
                          [[0, 0, 0],
                           [0, 5, 0],
                           [0, 0, 0]]), "2nd example"

    assert check_solution(checkio,
                          [[1, 15, 14, 4],
                           [12, 0, 0, 9],
                           [8, 0, 0, 5],
                           [13, 3, 2, 16]]), "3rd example"
