data = input()

remain = 0
answer = 0

for i in range(len(data)):
    if data[i] == '(':
        remain += 1
    else:
        remain -= 1
        if data[i - 1] == '(':
            answer += remain
        else:
            answer += 1

print(answer)