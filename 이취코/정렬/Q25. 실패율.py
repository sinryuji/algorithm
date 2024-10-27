# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    arr = []
    length = len(stages)

    stage_cnt = [0] * (N + 2)

    for stage in stages:
        stage_cnt[stage] += 1

    for i in range(1, N + 1):
        cnt = stage_cnt[i]
        arr.append((i, 0 if length == 0 else cnt / length))
        length -= cnt

    return list(i[0] for i in sorted(arr, key=lambda x: -x[1]))
