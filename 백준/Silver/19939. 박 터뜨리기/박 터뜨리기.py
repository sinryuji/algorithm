N, K = map(int, input().split())

x = K * (K + 1) // 2

if N < x:
    print(-1)
elif (N - x) % K == 0:
    print(K - 1)
else:
    print(K)
