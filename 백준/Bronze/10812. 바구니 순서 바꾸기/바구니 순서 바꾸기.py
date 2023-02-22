n, m = map(int, input().split())
basket = [i for i in range(1, n + 1)]
for _ in range(m):
    i, j, k = map(int, input().split())
    i -= 1; j -= 1; k -=1
    basket = basket[:i] + basket[k:j+1] + basket[i:k] + basket[j+1:]
print(*basket)