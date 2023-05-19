import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x : (x[1], x[0]))

cnt = 0
end = 0
for i, j in arr:
    if i >= end:
        end = j
        cnt += 1
        
print(cnt)