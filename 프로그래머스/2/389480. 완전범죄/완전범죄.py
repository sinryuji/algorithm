def solution(info, n, m):
    info_len = len(info)
    dp = [[[False] * m for _ in range(n)] for _ in range(info_len + 1)]
    dp[0][0][0] = True
    
    for i, (info_a, info_b) in enumerate(info):
        for a in range(n):
            for b in range(m):
                if dp[i][a][b]:
                    na = a + info_a
                    nb = b + info_b
                    if na < n:
                        dp[i+1][na][b] = True
                    if nb < m:
                        dp[i+1][a][nb] = True
                        
    for a in range(n):
        for b in range(m):
            if dp[info_len][a][b]:
                return a
    
    return -1