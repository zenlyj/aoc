def parse(s):
    return [int(c) for c in s.split(':')[1].strip().split()]

def solve():
    f = open('in.txt', 'r')
    time, distance = parse(f.readline()), parse(f.readline())
    res = 1
    for t, d in zip(time, distance):
        ways = 0
        for i in range(1, t):
            remain = t-i
            if remain*i > d:
                ways += 1
        res = res * ways
    return res

print(solve())
