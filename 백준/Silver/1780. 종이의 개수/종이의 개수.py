def solution(x, y, r):
    flag = paper[y][x]
    if r == 1:
        count[flag + 1] += 1
        return
    
    t = r // 3
    for i in range(y, y + r):
        for j in range(x, x + r):
            if paper[i][j] != flag:
                solution(x, y, t)
                solution(x, y + t, t)
                solution(x, y + t + t, t)
                solution(x + t, y, t)
                solution(x + t, y + t, t)
                solution(x + t, y + t + t, t)
                solution(x + t + t, y, t)
                solution(x + t + t, y + t, t)
                solution(x + t + t, y + t + t, t)
                return
                
    count[flag + 1] += 1

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
count = [0, 0, 0]
solution(0, 0, n)

print(*count, sep = '\n')