papers = [0] + [int(input()) for _ in range(6)]

answer = 0
while papers[6] > 0:
    papers[6] -= 1
    answer += 1

while papers[5] > 0:
    papers[5] -= 1
    answer += 1
    cnt = 11
    while papers[1] > 0 and cnt > 0:
        papers[1] -= 1
        cnt -= 1

while papers[4] > 0:
    papers[4] -= 1
    answer += 1
    cnt = 20
    while papers[2] > 0 and cnt > 0:
        papers[2] -= 1
        cnt -= 4
    while papers[1] > 0 and cnt > 0:
        papers[1] -= 1
        cnt -= 1

while papers[3] > 0:
    papers[3] -= 1
    answer += 1
    cnt = 27
    while papers[3] > 0 and cnt > 0:
        papers[3] -= 1
        cnt -= 9
    if cnt == 27:
        two_cnt = 5
    elif cnt == 18:
        two_cnt = 3
    elif cnt == 9:
        two_cnt = 1
    else:
        two_cnt = 0
    while papers[2] > 0 and two_cnt > 0 and cnt > 0:
        papers[2] -= 1
        two_cnt -= 1
        cnt -= 4
    while papers[1] > 0 and cnt > 0:
        papers[1] -= 1
        cnt -= 1

while papers[2] > 0:
    papers[2] -= 1
    answer += 1
    cnt = 32
    while papers[2] > 0 and cnt > 0:
        papers[2] -= 1
        cnt -= 4
    while papers[1] > 0 and cnt > 0:
        papers[1] -= 1
        cnt -= 1

while papers[1] > 0:
    papers[1] -= 1
    answer += 1
    cnt = 35
    while papers[1] > 0 and cnt > 0:
        papers[1] -= 1
        cnt -= 1

print(answer)