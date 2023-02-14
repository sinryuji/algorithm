n = int(input())
flag = False
for i in range(1, n + 1):
    sum = i
    for j in str(i):
        sum += int(j)
    if sum == n:
        print(i)
        flag = True
        break
if flag == False:
    print(0)