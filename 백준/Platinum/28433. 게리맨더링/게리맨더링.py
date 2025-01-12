import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    seq = list(map(int, input().split()))

    tmp = pos_cnt = neg_cnt = 0
    for num in seq:
        if num > 0:
            if tmp > 0:
                pos_cnt += 1
                tmp = num
            else:
                if num + tmp > 0:
                    tmp += num
                else:
                    neg_cnt += 1
                    tmp = num
        else:
            if tmp > 0:
                if num + tmp > 0:
                    tmp += num
                else:
                    pos_cnt += 1
                    tmp = num
            else:
                tmp += num

    if tmp > 0:
        pos_cnt += 1
    else:
        neg_cnt += 1

    if pos_cnt > neg_cnt:
        print('YES')
    else:
        print('NO')
