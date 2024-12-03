n = int(input())
result = [0] * 10
num = 1

def make_nine(number):
    while number % 10 != 9:
        for i in str(number):
            result[int(i)] += num
        number -= 1
    return number

while n > 0:
    n = make_nine(n)
    
    if n < 0:
        for i in range(n + 1):
            result[i] += num
    else:
        for i in range(10):
            result[i] += (n // 10 + 1) * num
    
    result[0] -= num
    num *= 10
    n //= 10
    
print(*result)