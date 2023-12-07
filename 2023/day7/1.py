from functools import cmp_to_key
import collections

powers = {
    'A' : 20,
    'K' : 19,
    'Q' : 18,
    'J' : 17,
    'T' : 16,
    '9' : 9,
    '8' : 8,
    '7' : 7,
    '6' : 6,
    '5' : 5,
    '4' : 4,
    '3' : 3,
    '2' : 2
}

def is_five_of_kind(s):
    return len(set(list(s))) == 1

def is_four_of_kind(s):
    count = collections.Counter(list(s))
    if len(count) != 2:
        return False
    vals = count.values()
    return (1 in vals) and (4 in vals)

def is_full_house(s):
    count = collections.Counter(list(s))
    if len(count) != 2:
        return False
    vals = count.values()
    return (2 in vals) and (3 in vals)

def is_three_of_kind(s):
    count = collections.Counter(list(s))
    if len(count) != 3:
        return False
    vals = count.values()
    return (3 in vals)

def is_two_pair(s):
    count = collections.Counter(list(s))
    if len(count) != 3:
        return False
    vals = count.values()
    val_count = collections.Counter(vals)
    if len(val_count) != 2:
        return False
    if 1 not in val_count or val_count[1] != 1:
        return False
    if 2 not in val_count or val_count[2] != 2:
        return False
    return True

def is_one_pair(s):
    count = collections.Counter(list(s))
    if len(count) != 4:
        return False
    vals = count.values()
    val_count = collections.Counter(vals)
    if len(val_count) != 2:
        return False
    if 1 not in val_count or val_count[1] != 3:
        return False
    if 2 not in val_count or val_count[2] != 1:
        return False
    return True

def first_compare(x, y):
    for s, v in zip(x, y):
        if powers[s] == powers[v]:
            continue
        return -1 if powers[s] > powers[v] else 1
    return 0

def compare(x, y):
    x, y = list(x[0]), list(y[0])   
    fns = [is_five_of_kind, is_four_of_kind, is_full_house, is_three_of_kind, is_two_pair, is_one_pair]
    x_apply, y_apply = [fn(x) for fn in fns], [fn(y) for fn in fns]
    for xx, yy in zip(x_apply, y_apply):
        if xx and not yy:
            return -1
        if yy and not xx:
            return 1
    return first_compare(x, y)

def solve():
    f = open('in.txt', 'r')
    hands = []
    for l in f:
        hands.append(l.split())
    hands = sorted(hands, key=cmp_to_key(compare), reverse=True)
    i = 1
    res = 0
    for hand in hands:
        res += i * int(hand[1])
        i += 1
    return res

print(solve())

