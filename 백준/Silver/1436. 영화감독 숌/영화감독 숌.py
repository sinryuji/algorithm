n = int(input())
cnt = 0
name = 666
while True:
    if '666' in str(name):
        cnt += 1
    if cnt == n:
        print(name)
        break
    name += 1