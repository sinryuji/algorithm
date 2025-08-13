s = input()

UCPC = 'UCPC'
idx = 0
for c in s:
    if UCPC[idx] == c:
        idx += 1
    if idx == 4:
        break
        
if idx == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')