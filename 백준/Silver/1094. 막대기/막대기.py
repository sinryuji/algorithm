x = int(input())
sticks = [64, 32, 16, 8, 4, 2, 1]
count = 0

for i in range(len(sticks)):
    if x >= sticks[i]:
        count += 1
        x -= sticks[i]
        
    if x == 0:
        break
        
print(count)