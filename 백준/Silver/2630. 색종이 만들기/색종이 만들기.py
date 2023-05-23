n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

white = 0
blue = 0

def check(x, y, r):
    global white, blue
    
    if r == 1:
        if paper[y][x] == 1:
            blue += 1
        else:
            white += 1
        return True

    for i in range(y, y + r):
        for j in range(x, x + r):
            if paper[i][j] != paper[y][x]:
                return False
                
    if paper[y][x] == 1:
        blue += 1
    else:
        white += 1
    return True
    
    
def solution(x, y, r):
    if check(x, y, r):
        return;
    else:
        half = r // 2
        solution(x, y, half)
        solution(x + half, y, half)
        solution(x, y + half, half)
        solution(x + half, y + half, half)
                 
solution(0, 0, n);
print(white)
print(blue)