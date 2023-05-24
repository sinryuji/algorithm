def solution(x, y, r):
    global comp
    global ret
    flag = data[y][x]

    if r == 1:
        ret += flag
        return
    
    h = r // 2
    for i in range(y, y + r):
        for j in range(x, x + r):
            if data[i][j] != flag:
                ret += "("
                solution(x, y, h)
                solution(x + h, y, h)
                solution(x, y + h, h)
                solution(x + h, y + h, h)
                ret += ")"
                return
    ret += flag

n = int(input())
data = [list(input()) for _ in range(n)]
ret = ""

solution(0, 0, n)
print(ret)