n, m = map(int, input().split())
card = sorted(list(map(int, input().split())), reverse = True)
ret = 0
for i in range(len(card) - 2):
    for j in range(i + 1, len(card) - 1):
        for k in range(j + 1, len(card)):
            sum = card[i] + card[j] + card[k]
            if sum <= m and sum > ret:
                ret = sum
                break
print(ret)