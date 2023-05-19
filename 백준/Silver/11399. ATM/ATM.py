n = int(input())
p = sorted(list(map(int, input().split())))

ret  = 0
for i in range(1, n + 1):
    ret += sum(p[:i])
    
print(ret)