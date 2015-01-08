def capture(matrix):
    num = len(matrix)
    visited = []
    time = [10000000] * num
    time[0] = 0
    now = 0
    while len(visited) != num - 1:
        visited.append(now)
        neighbors = [i for i in range(num) if matrix[now][i] == 1 and i not in visited]
        for n in neighbors:
            if time[now] + matrix[n][n] < time[n]:
                time[n] = time[now] + matrix[n][n]
        now = min([(i, time[i]) for i in range(num) if i not in visited], key=lambda a: a[1])[0]
    return max(time)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
