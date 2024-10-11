# https://school.programmers.co.kr/learn/courses/30/lessons/42891

import heapq

def solution(food_times, k):
    q = []
    s = 0
    size = len(food_times)
    for i in range(size):
        s += food_times[i]
        heapq.heappush(q, (food_times[i], i + 1))

    if s <= k:
        return -1

    total = 0
    prev = 0
    while total + ((q[0][0] - prev) * size) <= k:
        now = heapq.heappop(q)[0]
        total += (now - prev) * size
        size -= 1
        prev = now

    q.sort(key=lambda x: x[1])
    return q[(k - total) % size][1]
