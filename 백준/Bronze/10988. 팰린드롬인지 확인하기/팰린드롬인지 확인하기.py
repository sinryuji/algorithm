str = input()
mid = len(str) // 2
left = str[:mid]
if len(str) % 2 == 0:
    mid -= 1
right = str[:mid:-1]
print(1) if left == right else print(0)