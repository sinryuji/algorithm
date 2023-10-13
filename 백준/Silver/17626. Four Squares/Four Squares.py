n = int(input())
arr = [0 if i ** 0.5 % 1 else 1 for i in range(n + 1)]

ans = 4
for i in range(1, int(n ** 0.5) + 1):
    if arr[n]:
        ans = 1
        break
    elif arr[n - i ** 2]:
        ans = 2
        break
    else:
        for j in range(1, int((n - i ** 2) ** 0.5) + 1):
            if arr[(n - i ** 2) - j ** 2]:
                ans = 3
                break

print(ans)