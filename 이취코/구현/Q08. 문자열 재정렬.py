S = input()

num = 0
answer = []
for c in S:
    if c.isdigit():
        num += int(c)
    else:
        answer.append(c)

answer.sort()
if num != 0:
    answer.append(str(num))

print(''.join(answer))