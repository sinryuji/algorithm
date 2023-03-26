import sys
input = sys.stdin.readline

n, k = map(int,input().split())
tempers = list(map(int, input().split()))

result = []
result.append(sum(tempers[:k]))

for i in range(n - k):
    result.append(result[i] - tempers[i] + tempers[k + i])

print(max(result))