import functools
import math

def read_until_break(f):
    s = ''
    inp = f.readline()
    while inp != '\n':
        s += inp
        inp = f.readline()
    return s

def parse_network(s):
    mappings = s.split('\n')
    mappings = [m for m in mappings if m != '']
    adjList = {}
    for mapping in mappings:
        split = mapping.split('=')
        src = split[0].strip()
        dst = split[1].strip()
        dst = dst[1:len(dst)-1].split(',')
        dst = [d.strip() for d in dst]
        adjList.setdefault(src, dst)
    return adjList

def get_all_start(lst):
    return [s for s in lst if s[-1] == 'A']

def is_end(curr):
    return curr[-1] == 'Z'

def lcm(x, y):
    return abs(x*y) // math.gcd(x, y)

def solve():
    f = open('in.txt', 'r')
    instructions = read_until_break(f).strip()
    network = read_until_break(f)
    adjList = parse_network(network)
    direction_map = {
        'L' : 0,
        'R' : 1
    }
    all_steps, num_instr = [], len(instructions)
    all_start = get_all_start(adjList.keys())
    for curr in all_start:
        steps = 0
        while not is_end(curr):
            i = instructions[steps%num_instr]
            curr = adjList[curr][direction_map[i]]
            steps += 1
        all_steps.append(steps)
    return functools.reduce(lambda x, y: lcm(x, y), all_steps)

print(solve())
