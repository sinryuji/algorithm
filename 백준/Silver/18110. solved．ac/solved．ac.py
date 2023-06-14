import sys

def round_off(n):
    return int(n) + (1 if n - int(n) >= 0.5 else 0)

n = int(sys.stdin.readline())
if n == 0:
    print(0)
else: 
    d = sorted(list(map(int, sys.stdin.readlines())))
    cut = round_off(n * 0.15)
    ret = d[cut:n-cut]
    print(round_off(sum(ret) / len(ret)))