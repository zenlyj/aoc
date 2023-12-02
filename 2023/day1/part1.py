def calibrate(s):
    s = [c for c in s if c.isdigit()]
    return int(s[0] + s[-1])

def solve():
    f = open("1-in.txt", "r")
    res = 0
    for l in f:
        res += calibrate(l)
    return res

print(solve())
