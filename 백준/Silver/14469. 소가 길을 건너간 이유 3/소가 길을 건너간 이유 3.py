import sys

input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort()

time = 0
for a, b in arr:
    time = max(time, a)
    time += b
    
print(time)