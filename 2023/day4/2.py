import math

def parse(line):
    split = line.split(':')
    card_detail, numbers = split[0], split[1]
    card_num = card_detail.split()[1]
    split = numbers.split('|')
    winning, owned = split[0].strip(), split[1].strip()
    return int(card_num), winning.split(), owned.split()

def intersection(s, v):
    winning_set = set(s)
    return [n for n in v if n in winning_set]

def solve():
    f = open('in.txt', 'r')
    dp = [1]*1000
    num_card = 0
    for l in f:
        card, winning, owned = parse(l)
        intersect = intersection(winning, owned)
        for i in range(len(intersect)):
            if card+i >= len(dp):
                break
            dp[card+i] += dp[card-1]
        num_card += 1
    return sum(dp[:num_card])

print(solve())
