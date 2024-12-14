N = int(input())

data = []
max_country = 0
for _ in range(N):
    a, b, c = map(int, input().split())
    max_country = max(a, max_country)
    data.append((a, b, c))
data.sort(key=lambda x: -x[2])
country_count = [0] * (max_country + 1)

cnt = 0
for a, b, c in data:
    if cnt == 3:
        break
    if country_count[a] < 2:
        country_count[a] += 1
        print(a, b)
        cnt += 1
    else:
        continue
