import sys

input = sys.stdin.readline

N, H = map(int, input().split())
up = [0] * (H + 1)
down = [0] * (H + 1)

for i in range(N):
    h = int(input())
    if i % 2 == 0:
        down[h] += 1
    else:
        up[h] += 1
        
for i in range(H - 1, 0, -1):
    up[i] += up[i + 1]
    down[i] += down[i + 1]
    
min_cnt = 0
min_num = sys.maxsize
for i in range(1, H + 1):
    s = up[H - i + 1] + down[i]
    if s == min_num:
        min_cnt += 1
    elif s < min_num:
        min_cnt = 1
        min_num = s
        
print(min_num, min_cnt)