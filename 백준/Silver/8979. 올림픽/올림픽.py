N, K = map(int, input().split())
medals = dict()
for _ in range(N):
    n, g, s, b = map(int, input().split())
    medals[n] = [g, s, b]

sorted_medals = sorted(medals.items(), key=lambda item: item[1])

answer = [0] * (N + 1)
rank = 0
tmp = 0
prev = []
for key, val in sorted_medals:
    if val != prev:
        rank += tmp + 1
        tmp = 0
    else:
        tmp += 1
    answer[key] = rank
    prev = val

print(answer[K])
