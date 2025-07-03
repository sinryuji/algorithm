N, L = map(int, input().split())
heights = sorted(list(map(int, input().split())))

for h in heights:
    if L < h:
        break
    L += 1
        
print(L)