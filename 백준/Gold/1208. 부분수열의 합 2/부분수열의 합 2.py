import sys
from itertools import combinations

input = sys.stdin.readline


def solve():
    N, S = map(int, input().split())
    nums = sorted(list(map(int, input().split())))

    t1 = nums[:N // 2]
    t2 = nums[N // 2:]

    t1_sum_list = list()
    t2_sum_list = list()

    for i in range(len(t1) + 1):
        for com in combinations(t1, i):
            t1_sum_list.append(sum(com))
    t1_sum_list.sort()
    t1_len = len(t1_sum_list)

    for i in range(len(t2) + 1):
        for com in combinations(t2, i):
            t2_sum_list.append(sum(com))
    t2_sum_list.sort(reverse=True)
    t2_len = len(t2_sum_list)

    answer = 0
    lt, rt = 0, 0
    while lt < t1_len and rt < t2_len:
        lp, rp = t1_sum_list[lt], t2_sum_list[rt]
        t_sum = lp + rp

        if t_sum > S:
            rt += 1
        elif t_sum < S:
            lt += 1
        else:
            tlt, trt = lt, rt
            while tlt < t1_len and t1_sum_list[tlt] == lp:
                tlt += 1
            while trt < t2_len and t2_sum_list[trt] == rp:
                trt += 1
            answer += (tlt - lt) * (trt - rt)
            lt, rt = tlt, trt

    if S == 0:
        answer -= 1
    print(answer)


solve()