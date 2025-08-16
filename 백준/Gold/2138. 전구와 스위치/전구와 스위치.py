N = int(input())
cur = list(map(int, input()))
goal = list(map(int, input()))
MAX = float('inf')

def search(cnt, cur, goal):
    for i in range(1, N):
        if cur[i - 1] != goal[i - 1]:
            cur[i - 1] = 1 - cur[i - 1]
            cur[i] = 1 - cur[i]
            if i < N - 1:
                cur[i + 1] = 1 - cur[i + 1]
            cnt += 1

    for i in range(N):
        if cur[i] != goal[i]:
            return MAX
    return cnt

ans = MAX
ans = min(ans, search(0, cur.copy(), goal.copy()))
cur[0] = 1 - cur[0]
cur[1] = 1 - cur[1]
ans = min(ans, search(1, cur.copy(), goal.copy()))

print(ans if ans < MAX else -1)