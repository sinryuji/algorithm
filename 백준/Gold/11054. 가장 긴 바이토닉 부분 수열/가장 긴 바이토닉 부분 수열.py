n = int(input())
a = list(map(int, input().split()))

increase = [1] * n
decrease = [1] * n
result = [0] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            increase[i] = max(increase[i], increase[j] + 1)
for i in range(n - 1, -1, -1):
    for j in range(i, n):
        if a[i] > a[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)
    result[i] = increase[i] + decrease[i] - 1


print(max(result))