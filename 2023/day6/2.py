def parse(s):
    return int(''.join(s.split(':')[1].strip().split()))

def solve():
    f = open('in.txt', 'r')
    time, distance = parse(f.readline()), parse(f.readline())
    ways = 0
    for i in range(1, time):
        remain = time-i
        if remain*i > distance:
            ways += 1
    return ways

print(solve())
