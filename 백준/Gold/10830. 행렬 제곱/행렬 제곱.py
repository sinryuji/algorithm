def mul_matrix(a, b):
    n = len(a)
    ret = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            x = 0
            for k in range(n):
                x += a[i][k] * b[k][j]
            ret[i][j] = x % 1000
    return ret
    
def solution(a, b):
    if b == 1:
        for i in range(len(a)):
            for j in range(len(a)):
                a[i][j] %= 1000
        return a
    tmp = solution(a, b // 2)
    if b % 2 == 0:
        return mul_matrix(tmp, tmp)
    else:
        return mul_matrix(mul_matrix(tmp, tmp), a)
    
n, b = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(n)]
ret = solution(m, b)

for i in range(n):
    print(*ret[i], sep = ' ')