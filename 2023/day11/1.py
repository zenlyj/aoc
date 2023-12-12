from collections import deque

def expand_grid(grid):
    expanded = []
    for row in grid:
        if all([c == '.' for c in row]):
            expanded.append(['.']*len(grid[0]))
        expanded.append([c for c in row])
    col_offset = 0
    for j in range(len(grid)):
        col = [grid[i][j] for i in range(len(grid))]
        if all([c == '.' for c in col]):
            for i in range(len(expanded)):
                expanded[i].insert(j+1+col_offset, '.')
            col_offset += 1 
    return expanded

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

def bfs(grid, src, dst):
    q = deque()
    q.append(src)
    dist = 0
    DIRECTIONS = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]
    visited = set()
    while q:
        level = []
        while q:
            level.append(q.popleft())
        for curr in level:
            visited.add(curr)    
            if curr == dst:
                return dist
            for d in DIRECTIONS:
                dx, dy = curr[0]+d[0], curr[1]+d[1]
                if dx < 0 or dx >= len(grid) or dy < 0 or dy >= len(grid[0]):
                    continue
                if (dx, dy) in visited:
                    continue
                q.append((dx, dy))
        dist += 1
    return -1

def manhattan_dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def solve():
    f = open('in.txt', 'r')
    grid = [list(l.strip()) for l in f]
    expanded = expand_grid(grid)
    nodes = mark_nodes(expanded)
    for row in expanded:
        print(''.join(row))
    res = 0
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            res += manhattan_dist(nodes[i], nodes[j])
    return res

print(solve())
