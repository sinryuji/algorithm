import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dnas = [list(input().rstrip()) for _ in range(N)]

ans_dna = ''
ans_dist = 0
for i in range(M):
    d = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for j in range(N):
        d[dnas[j][i]] += 1
    sort_d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    ans_dna += sort_d[0][0]
    ans_dist += N - sort_d[0][1]

print(ans_dna)
print(ans_dist)