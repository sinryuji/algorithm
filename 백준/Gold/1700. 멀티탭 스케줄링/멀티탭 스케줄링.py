import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
mt = []
for i in range(K):
    if arr[i] in mt:
        continue
    if len(mt) < N:
        mt.append(arr[i])
        continue

    priority = []
    for v in mt:
        if v in arr[i:]:
            priority.append(arr[i:].index(v))
        else:
            priority.append(101)
    target = priority.index(max(priority))
    mt.remove(mt[target])
    mt.append(arr[i])
    ans += 1

print(ans)
