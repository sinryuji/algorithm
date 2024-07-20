n = int(input())
classes = []
same = [0] * n
for i in range(n):
    classes.append(list(map(int, input().split())))
    same[i]= [0] * n
    
for i in range(5):
    for j in range(n):
        for k in range(j + 1, n):
            if classes[j][i] == classes[k][i]:
                same[k][j] = 1
                same[j][k] = 1
                
cnt = []
for s in same:
    cnt.append(s.count(1))
    
print(cnt.index(max(cnt)) + 1)