n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

first = data[-1]
second = data[-2]

result = 0

while True:
    for _ in range(k): # 가장 큰 수를 k번 더하기
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1

print(result)
