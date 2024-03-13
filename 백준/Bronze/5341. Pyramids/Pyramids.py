while True:
    n = int(input())
    if n == 0:
        break
    answer = 0
    while n > 0:
        answer += n
        n -= 1
    print(answer)