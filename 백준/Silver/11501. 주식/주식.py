import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    
    s = 0
    tmp = 0
    for p in arr[::-1]:
        if p > tmp:
            tmp = p
        else:
            s += tmp - p
        
    print(s)