import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = 999999
house = []
chick = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            house.append([i, j])
        elif graph[i][j] == 2:
            chick.append([i, j])

for chi in combinations(chick, M):
    temp = 0
    for h in house:
        chi_len = 999
        for j in range(M):
            chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
        temp += chi_len
    answer = min(answer, temp)

print(answer)