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

def solve():
    f = open('in.txt', 'r')
    instructions = read_until_break(f).strip()
    network = read_until_break(f)
    adjList = parse_network(network)
    direction_map = {
        'L' : 0,
        'R' : 1
    }
    steps, num_instr = 0, len(instructions)
    curr, end = 'AAA', 'ZZZ'
    while curr != end:
        i = instructions[steps%num_instr]
        curr = adjList[curr][direction_map[i]]
        steps += 1
    return steps

print(solve())
