import sys

input = sys.stdin.readline


def pos(now):
    for j in range(1, N):
        if abs(now[j] - now[j - 1]) > 1:
            return False
        if now[j] < now[j - 1]:
            for k in range(L):
                if j + k >= N or used[j + k] or now[j] != now[j + k]:
                    return False
                if now[j] == now[j + k]:
                    used[j + k] = True
        elif now[j] > now[j - 1]:
            for k in range(L):
                if j - k - 1 < 0 or now[j - 1] != now[j - k - 1] or used[j - k - 1]:
                    return False
                if now[j - 1] == now[j - k - 1]:
                    used[j - k - 1] = True
    return True


N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for i in range(N):
    used = [False] * N
    if pos(graph[i]):
        answer += 1

for i in range(N):
    used = [False] * N
    if pos([graph[j][i] for j in range(N)]):
        answer += 1

print(answer)
