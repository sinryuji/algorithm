n = int(input())
p = 1000000007

def mul_matrix(a, b):
    n = len(a)
    ret = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            x = 0
            for k in range(n):
                x += a[i][k] * b[k][j]
            ret[i][j] = x % p
    return ret
    
def solution(a, b):
    if b == 1:
        for i in range(len(a)):
            for j in range(len(a)):
                a[i][j] %= p
        return a
    tmp = solution(a, b // 2)
    if b % 2 == 0:
        return mul_matrix(tmp, tmp)
    else:
        return mul_matrix(mul_matrix(tmp, tmp), a)

fib_matrix = [[1, 1],[1, 0]]
print(solution(fib_matrix, n)[0][1])