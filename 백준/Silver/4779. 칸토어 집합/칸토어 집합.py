import sys
input = sys.stdin.readline

def recur(start, x):
    global ret
    if x == 0:
        return
    for i in range(start + 3 ** (x - 1), start + 3 ** (x - 1) * 2):
        ret[i] = ' '
    recur(start, x - 1)
    recur(start + 3 ** (x - 1) * 2, x - 1)

while True:
    n = input()
    if n == "":
        break
    n = int(n)
    ret = ['-'] * 3 ** n
    recur(0, n)
    print(*ret, sep = '')