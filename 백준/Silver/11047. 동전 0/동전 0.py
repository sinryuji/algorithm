n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.reverse()
cnt = 0

while k > 0:
    for coin in coins:
        if k >= coin:
            cnt += k // coin
            k %= coin
            break

print(cnt)