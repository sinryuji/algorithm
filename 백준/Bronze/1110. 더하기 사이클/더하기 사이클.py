x = y = int(input())
count = 0
while True:
    x = (x % 10 * 10) + (x // 10 + x % 10) % 10
    count += 1
    if x == y:
        break
print(count)