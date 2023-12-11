N,S,E,W = 'NORTH', 'SOUTH', 'EAST', 'WEST'

DIRECTIONS = {
    (1, 0) : N,
    (-1, 0) : S,
    (0, 1) : W,
    (0, -1) : E
}

def get_next(grid, direction, pos):
    pipe = grid[pos[0]][pos[1]]
    x, y = pos[0], pos[1]
    if pipe == '|':
        if direction == N:
            return (N, (x+1, y))
        if direction == S:
            return (S, (x-1, y))
    if pipe == '-':
        if direction == W:
            return (W, (x, y+1))
        if direction == E:
            return (E, (x, y-1))
    if pipe == 'L':
        if direction == N:
            return (W, (x, y+1))
        if direction == E:
            return (S, (x-1, y))
    if pipe == 'J':
        if direction == W:
            return (S, (x-1, y))
        if direction == N:
            return (E, (x, y-1))
    if pipe == '7':
        if direction == W:
            return (N, (x+1, y))
        if direction == S:
            return (E, (x, y-1))
    if pipe == 'F':
        if direction == S:
            return (W, (x, y+1))
        if direction == E:
            return (N, (x+1, y))
    return (None, None)

def solve():
    f = open('in.txt', 'r')
    grid = [list(ln.strip()) for ln in f]
    m,n = len(grid), len(grid[0])

    def is_out_of_bounds(pos):
        return pos[0] < 0 or pos[0] >= m or pos[1] < 0 or pos[1] >= n

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 'S':
                start_point = (r,c)

    res = 0
    for d in DIRECTIONS:
        visited = 1
        curr_pos = (start_point[0]+d[0], start_point[1]+d[1])
        curr_direction = DIRECTIONS[d]
        while curr_pos and curr_direction and not is_out_of_bounds(curr_pos) and grid[curr_pos[0]][curr_pos[1]] != '.':
            if curr_pos == start_point:
                res = max(res, visited//2)
                break
            curr_direction, curr_pos = get_next(grid, curr_direction, curr_pos)
            visited += 1
    f.close()
    return res

print(solve())
