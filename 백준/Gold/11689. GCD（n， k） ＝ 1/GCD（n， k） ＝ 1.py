n = int(input())

answer = n
i = 2
while i ** 2 <= n:
    if n % i == 0:
        answer *= (1 - (1 / i))
        while not n % i:
            n //= i
    i += 1

if n > 1:
    answer *= 1 - 1 / n

print(round(answer))
