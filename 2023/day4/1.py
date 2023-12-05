import math

def parse(line):
    split = line.split(':')
    card_detail, numbers = split[0], split[1]
    card_num = card_detail.split()[1]
    split = numbers.split('|')
    winning, owned = split[0].strip(), split[1].strip()
    return card_num, winning.split(), owned.split()

def intersection(s, v):
    winning_set = set(s)
    return [n for n in v if n in winning_set]

def score(count):
    return int(2**(count-1))

def solve():
    f = open('in.txt', 'r')
    res = 0
    for l in f:
        card, winning, owned = parse(l)
        intersect = intersection(winning, owned)
        res += score(len(intersect))
    return res

print(solve())
