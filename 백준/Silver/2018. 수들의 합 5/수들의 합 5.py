import math

n = int(input())
end = 0
sum = 0
count = 0

    
for start in range(0, n):
    while sum < n and end < n :
        sum += end+1
        end += 1
    if sum == n:
        count += 1
    sum -= start+1
print(count)