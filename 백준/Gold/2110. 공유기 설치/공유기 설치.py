import sys

n, c = map(int, sys.stdin.readline().split())
h = sorted(list(map(int, sys.stdin.readlines())))

start = 1
end = h[-1] - h[0]
answer = 0
while start <= end:
    mid = (start + end) // 2
    cur = h[0]
    cnt = 1
    
    for i in range(1, len(h)):
        if h[i] >= cur + mid:
            cnt += 1
            cur = h[i]
    
    if cnt >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)