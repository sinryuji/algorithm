import sys

input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key = lambda x: (-x[1], x[0]))

ans = 0
checked = [False] * (1001)
for a, b in arr:
    for i in range(a, 0, -1):
        if not checked[i]:
            ans += b
            checked[i] = True
            break
        
print(ans)