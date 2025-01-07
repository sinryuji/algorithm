from collections import deque

def solution(queue1, queue2):
    total_len = len(queue1) + len(queue2)
    queue1, queue2 = deque(queue1), deque(queue2)
    q1s, q2s = sum(queue1), sum(queue2)
    s = q1s + q2s
    if s & 1:
        return -1
    s //= 2
    answer = 0
    while q1s != s:
        answer += 1
        if answer > total_len * 2:
            answer = -1
            break
        if q1s > q2s:
            n = queue1.popleft()
            q1s -= n
            q2s += n
            queue2.append(n)
        else:
            n = queue2.popleft()
            q1s += n
            q2s -= n
            queue1.append(n)
    return answer
            