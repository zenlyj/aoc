import re
from functools import cmp_to_key

def compare(s, v):
    if s[0] < v[0]:
        return -1
    elif s[0] > v[0]:
        return 1
    else:
        return 0

def digit_calibrate(s):
    res = []
    for i in range(len(s)):
        c = s[i]
        if c.isdigit():
            res.append((i, c))
    return res
        
def word_calibrate(s):
    mapping = {
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }
    
    res = []
    for word in mapping:
        pattern = re.compile(word) 
        for m in re.finditer(pattern, s):
            res.append((m.start(), mapping[word]))
    return sorted(res, key=cmp_to_key(compare))

def solve():
    f = open("2-in.txt", "r")
    res = 0
    for l in f:
        dc, wc = digit_calibrate(l), word_calibrate(l)
        if not dc:
            res += int(wc[0][1] + wc[-1][1])
        elif not wc:
            res += int(dc[0][1] + dc[-1][1])
        else:
            first = wc[0][1] if wc[0][0] < dc[0][0] else dc[0][1]
            second = wc[-1][1] if wc[-1][0] > dc[-1][0] else dc[-1][1]
            res += int(first+second)
    return res

print(solve())
