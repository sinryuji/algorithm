n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))

cost = 0
price = city[0]
for i in range(n - 1):
    if city[i] >= city[i + 1]:
        cost += price * road[i]
    else:
        price = city[i]
        cost += price * road[i]

print(cost)