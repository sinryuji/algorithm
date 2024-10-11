N, M = map(int, input().split())
weights = list(map(int, input().split()))

arr = [0] * (M + 1)

for weight in weights:
    arr[weight] += 1

answer = 0
for i in range(1, M + 1):
    N -= arr[i]
    answer += N * arr[i]

print(answer)