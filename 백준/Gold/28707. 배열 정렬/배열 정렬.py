import sys, heapq

input = sys.stdin.readline


def apply(arr, l, r):
    arr = list(arr)
    arr[l - 1], arr[r - 1] = arr[r - 1], arr[l - 1]
    return tuple(arr)


N = int(input())
A = tuple(map(int, input().split()))
M = int(input())
commands = []
for _ in range(M):
    commands.append(list(map(int, input().split())))

sorted_A = tuple(sorted(A))
q = [(0, A)]
visited = dict()
answer = -1
while q:
    cost, arr = heapq.heappop(q)
    if arr in visited:
        continue
    else:
        visited[arr] = True
    if arr == sorted_A:
        answer = cost
        break
    for l, r, c in commands:
        new_arr = apply(arr, l, r)
        heapq.heappush(q, (cost + c, new_arr))

print(answer)