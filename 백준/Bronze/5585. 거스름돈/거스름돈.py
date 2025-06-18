n = 1000 - int(input())

answer = 0
for i in [500, 100, 50, 10, 5, 1]:
    if n >= i:
        answer += n // i
        n %= i
        
print(answer)