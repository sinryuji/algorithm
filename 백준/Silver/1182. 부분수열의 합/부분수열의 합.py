from itertools import combinations

N, S = map(int, input().split())
seq = list(map(int, input().split()))

answer = 0
for i in range(1, N + 1):
    for per in combinations(seq, i):
        if sum(per) == S:
            answer += 1
            
print(answer)