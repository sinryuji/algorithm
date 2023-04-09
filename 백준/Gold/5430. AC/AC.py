import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = list(map(len, input().rstrip().replace('RR', '').split('R')))
    n = int(input())
    if n == 0:
        input()
        arr = []
    else:
        arr = input().strip('[]\n').split(',')

    front = sum(p[0::2])
    try:
        back = sum(p[1::2])
    except:
        back = 0

    if front + back > n:
        print('error')
        continue
    else:
        arr = arr[front:(n - back)]
    
    if (len(p) + 1) % 2 == 1:
        arr.reverse()
    print('[', ','.join(arr), ']', sep = '')