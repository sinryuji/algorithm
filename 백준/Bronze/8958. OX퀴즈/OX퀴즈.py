n = int(input())
list = [input() for _ in range(n)]
for line in list:
    sum = 0
    stack = 1;
    for ch in line:
        if ch == 'O':
            sum += stack
            stack += 1
        else:
            stack = 1
    print(sum)