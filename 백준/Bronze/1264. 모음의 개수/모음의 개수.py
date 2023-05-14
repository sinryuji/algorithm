vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while(True):
    s = input()
    if s == "#":
        break
    cnt = 0
    for c in s:
        if c in vowels:
            cnt += 1
    print(cnt)