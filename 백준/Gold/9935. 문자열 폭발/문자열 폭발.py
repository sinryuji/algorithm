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
        del s[-boom_len:]
            
if len(s) == 0:
    print("FRULA")
else:
    print(''.join(s))