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

def is_out_of_bounds(i, j, m, n):
    return i < 0 or i >= m or j < 0 or j >= n

def is_symbol(c):
    return not c.isdigit() and c != '.'

def solve():
    f = open('in.txt', 'r')
    arr = []
    res = 0
    for l in f:
        arr.append([c for c in l if c != '\n'])
    f.close()
    
    m, n = len(arr), len(arr[0])
    i = 0
    while i < m:
        j = 0
        while j < n:
            c = arr[i][j]
            if not c.isdigit():
                j += 1
                continue
            num = ''
            is_part_num = False
            while c.isdigit():
                for d in DIRECTIONS:
                    x, y = i+d[0], j+d[1]
                    is_part_num = is_part_num or (not is_out_of_bounds(x, y, m, n) and is_symbol(arr[x][y]))
                j += 1
                num += c
                if is_out_of_bounds(i, j, m, n):
                    break
                c = arr[i][j]
            if is_part_num:
                res += int(num)
        i += 1
    return res

print(solve())
