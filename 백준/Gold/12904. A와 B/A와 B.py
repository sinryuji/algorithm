s, t = list(input()), list(input())

ret = False
while t:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if s == t:
        ret = True
        break
        
print(int(ret))