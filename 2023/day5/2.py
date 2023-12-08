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

def get_mapped_values(seed_ranges, mapping):
    res = []
    for r in seed_ranges:
        res += split_range(r[0], r[1], mapping)
    return res

def split_range(start, end, mapping):
    split = []
    for m in mapping:
        dst, src, length = m[0], m[1], m[2]
        lim = src+length-1
        offset = dst-src
        if start >= src and end <= lim:
            split.append((start+offset, end+offset))
            break
        elif start >= src and start <= lim and end > lim:
            split.append((start+offset, lim+offset))
            split += split_range(lim+1, end, mapping)
            break
        elif start < src and end >= src and end <= lim:
             split += split_range(start, src-1, mapping)
             split.append((src+offset, end+offset))
             break
        elif start < src and end >= src and end > lim:
            split += split_range(start, src-1, mapping)
            split.append((src+offset, lim+offset))
            split += split_range(lim+1, end, mapping)
            break
    if not split:
        split.append((start, end))
    return split

def solve():
    f = open('in.txt', 'r')
    res = float('inf')
    MAPPING_LEVELS = 7
    seeds = parse_init(read_until_break(f))
    mappings = [parse_map(read_until_break(f)) for i in range(MAPPING_LEVELS)]
    for i in range(0, len(seeds), 2):
        seed_ranges = [(seeds[i], seeds[i]+seeds[i+1]-1)]
        for mapping in mappings:
            seed_ranges = get_mapped_values(seed_ranges, mapping)
        res = min(res, min([seed_range[0] for seed_range in seed_ranges]))
    f.close()
    return res

print(solve())
