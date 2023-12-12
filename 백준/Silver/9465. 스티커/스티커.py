import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    
    graph = []
    graph.append(list(map(int, input().split())))
    graph.append(list(map(int, input().split())))
    
    if n == 1:
        print(max(graph[0][0], graph[1][0]))
        continue
    
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = graph[0][0]
    dp[1][0] = graph[1][0]
    dp[0][1] = dp[1][0] + graph[0][1]
    dp[1][1] = dp[0][0] + graph[1][1]

    for i in range(2, n):
        for j in range(2):
            if j == 0:
                dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + graph[0][i]
            else:
                dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + graph[1][i]

    print(max(dp[0][n-1], dp[1][n-1]))