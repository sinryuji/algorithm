import sys

n = int(sys.stdin.readline())
seq = [int(i) for i in sys.stdin.readlines()]
stack = []
ret = []
i = 1

for num in seq:
    while i <= num:
        stack.append(i)
        ret.append('+')
        i += 1
    if stack.pop() != num:
        ret = ['NO']
        break
    ret.append('-')
print(*ret, sep = '\n')