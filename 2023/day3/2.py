DIRECTIONS = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
    [-1, -1],
    [1, -1],
    [-1, 1],
    [1, 1]
]

def get_val(arr, i, j):
    val = arr[i][j]
    left = j - 1
    while left >= 0:
        if not arr[i][left].isdigit():
            break
        val = arr[i][left] + val
        arr[i][left] = '.'
        left -= 1
    right = j + 1
    while right < len(arr[0]):
        if not arr[i][right].isdigit():
            break
        val += arr[i][right]
        arr[i][right] = '.'
        right += 1
    return int(val)

def is_out_of_bounds(i, j, m, n):
    return i < 0 or i >= m or j < 0 or j >= n

def solve():
    f = open('in.txt', 'r')
    arr = []
    res = 0
    for l in f:
        arr.append([c for c in l if c != '\n'])
    f.close()
    
    m, n = len(arr), len(arr[0])

    for i in range(m):
        for j in range(n):
            c = arr[i][j]
            if c != '*':
                continue
            adjacents = []
            for d in DIRECTIONS:
                x, y = i+d[0], j+d[1]
                if not is_out_of_bounds(x, y, m, n) and arr[x][y].isnumeric():
                    adjacents.append(get_val(arr, x, y))
            if len(adjacents) == 2:
                res += adjacents[0] * adjacents[1]

    return res

print(solve())
