def diff(arr):
    res = []
    for i in range(len(arr)-1):
        res.append(arr[i+1]-arr[i])
    return res

def solve():
    f = open('in.txt', 'r')
    res = 0
    for l in f:
        arr = l.split()
        arr = [int(c) for c in arr]
        seq = [arr]
        d = diff(arr)
        while not all([i == 0 for i in d]):
            seq.append(d)
            d = diff(d)
        seq = seq[::-1]
        accum = 0
        for s in seq:
            accum = s[0]-accum
        res += accum
    return res

print(solve())
