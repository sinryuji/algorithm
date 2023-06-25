n = int(input())
w = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

dp = [[0 for j in range((i + 1) * 500 + 1)] for i in range(n + 1)]
answer = []

def solve(num, weight):
    if num > n:
        return
    if dp[num][weight]:
        return
    
    dp[num][weight] = 1
    
    solve(num + 1, weight)
    solve(num + 1, weight + w[num - 1])
    solve(num + 1, abs(weight - w[num - 1]))

solve(0, 0)
    
for i in b:
    if i > 30 * 500:
        answer.append('N')
    elif dp[n][i]:
        answer.append('Y')
    else:
        answer.append('N')
        
print(*answer)