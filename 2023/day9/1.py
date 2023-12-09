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
        res += sum(s[-1] for s in seq)
    return res

print(solve())
