import sys
input = sys.stdin.readline

str = input().rstrip()
boom = input().rstrip()
s = []
boom_len = len(boom)
last_char = boom[-1]

for c in str:
    s.append(c)
    if last_char == c and ''.join(s[-boom_len:]) == boom:
        for _ in range(boom_len):
            s.pop()
            
if len(s) == 0:
    print("FRULA")
else:
    print(''.join(s))