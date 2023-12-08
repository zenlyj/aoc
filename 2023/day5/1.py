def read_until_break(f):
    l = f.readline()
    s = ''
    while l != '\n':
        s += l
        l = f.readline()
    return s.strip()

def parse_init(s):
    split = s.split(':')
    return [int(c) for c in split[1].strip().split()]

def parse_map(s):
    mappings = s.split('\n')[1:]
    return [[int(c) for c in m.split()] for m in mappings]

def get_mapped_value(value, mapping):
    for m in mapping:
        dst, src, length = m[0], m[1], m[2]
        if value >= src and value < src+length:
            return value+(dst-src)
    return value

def solve():
    f = open('in.txt', 'r')
    res = float('inf')
    MAPPING_LEVELS = 7
    seeds = parse_init(read_until_break(f))
    mappings = [parse_map(read_until_break(f)) for i in range(MAPPING_LEVELS)]
    for seed in seeds:
        mapped = seed
        for mapping in mappings:
            mapped = get_mapped_value(mapped, mapping)
        res = min(res, mapped) 
    f.close()
    return res

print(solve())
