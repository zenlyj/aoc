def mark_nodes(grid):
    idx = 0
    nodes = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                grid[i][j] = str(idx)
                idx += 1
                nodes.append((i, j))
    return nodes

def manhattan_dist(a, b, offset):
    return abs(a[0]-b[0])+offset[0] + abs(a[1]-b[1])+offset[1]

def empty_rows(grid):
    res = set()
    for i in range(len(grid)):
        row = grid[i]
        if all([c == '.' for c in row]):
            res.add(i)
    return res

def empty_cols(grid):
    res = set()
    for j in range(len(grid[0])):
        col = [grid[i][j] for i in range(len(grid))]
        if all([c == '.' for c in col]):
            res.add(j)
    return res

def solve():
    f = open('in.txt', 'r')
    grid = [list(l.strip()) for l in f]
    nodes = mark_nodes(grid)
    res = 0
    rows_e, cols_e = empty_rows(grid), empty_cols(grid)
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            start_x = min(nodes[i][0], nodes[j][0])
            end_x = max(nodes[i][0], nodes[j][0])
            start_y = min(nodes[i][1], nodes[j][1])
            end_y = max(nodes[i][1], nodes[j][1])
            offset_x = len([i for i in range(start_x, end_x) if i in rows_e])
            offset_y = len([i for i in range(start_y, end_y) if i in cols_e])
            expansion = int(1e6)
            res += manhattan_dist(nodes[i], nodes[j], (offset_x*expansion-offset_x, offset_y*expansion-offset_y))
    return res

print(solve())
