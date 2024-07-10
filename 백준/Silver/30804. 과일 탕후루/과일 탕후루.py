n = int(input())
fruit = list(map(int, input().split()))

left, right = 0, 1
kind = [fruit[0]]
answer = 0
next_left = 0
while right < n:
    if len(kind) == 1:
        if fruit[right] not in kind:
            kind.append(fruit[right])

    else:
        if fruit[right] not in kind:
            answer = max(answer, right - left)

            for i in range(len(kind)):
                if kind[i] != fruit[next_left]:
                    kind.pop(i)
                    break

            kind.append(fruit[right])
            left = next_left

    if fruit[right - 1] != fruit[right]:
        next_left = right
    right += 1

answer = max(answer, n-left)
print(answer)