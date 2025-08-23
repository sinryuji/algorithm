import sys
from collections import defaultdict
from heapq import heappop, heappush

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())

    values_count = defaultdict(int) # 중복되는 값들을 모두 힙큐에 넣지 않고 dict를 통해 따로 개수 세주기
    values = list(map(int, input().split()))

    heap = []
    for value in values:
        values_count[value] += 1
        if values_count[value] == 1:
            heappush(heap, value)

    ans = 0
    while len(heap) > 1 or (len(heap) == 1 and values_count[heap[0]] > 1): # 힙큐의 길이가 1보다 크거나 1인데 그 개수가 2개 이상인 경우 계속 반복
        min_value = heappop(heap)
        min_value_count = values_count[min_value]
        if min_value_count > 1: # 최소값의 개수가 2개 이상이면 
            ans += min_value * 2 * (min_value_count >> 1) # 최소값 + 최소값을 힙큐에 추가하고 최소값 총합 만큼을 답에 더하기
            if min_value * 2 not in values_count: # 최소값 + 최소값이 힙큐에 없으면 힙큐, dict에 추가
                values_count[min_value * 2] = 0
                heappush(heap, min_value * 2)
            values_count[min_value * 2] += (min_value_count >> 1)

            if min_value_count & 1: # 최소값의 개수가 홀수면 1개는 남기기
                values_count[min_value] = 1
                heappush(heap, min_value)
            else:
                del values_count[min_value]
        else: # 최소값의 개수가 1개면
            del values_count[min_value]
            min_value2 = heappop(heap) # 그 다음 최소값을 뽑고
            sum_value = min_value + min_value2
            ans += min_value + min_value2 # 최소값 + 그 다음 최소값 만큼 더하기
            if sum_value not in values_count:
                values_count[sum_value] = 0
                heappush(heap, sum_value)
            values_count[sum_value] += 1

            if values_count[min_value2] > 1: # 그 다음 최소값이 2개 이상이면 1개 줄여주기
                values_count[min_value2] -= 1
                heappush(heap, min_value2)
            else:
                del values_count[min_value2] # 아니면 삭제

    print(ans)