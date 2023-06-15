import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
time = sys.maxsize
floor = 0

for target in range(257):
    max_target, min_target = 0, 0
    
    for i in range(n):
        for j in range(m):
            if l[i][j] >= target:
                max_target += l[i][j] - target
            else:
                min_target += target - l[i][j]
                
    if max_target + b >= min_target:
        if max_target * 2 + min_target <= time:
            time = max_target * 2 + min_target
            floor = target
            
print(time, floor)