import sys
import heapq
input = sys.stdin.readline

def is_empty(nums):
    for key, val in nums.items():
        if val > 0:
            return False
    return True

T = int(input())

for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    nums = dict()

    for _ in range(k):
        op, num = input().split()
        num = int(num)

        if op == 'I':
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1
                heapq.heappush(min_heap, num)
                heapq.heappush(max_heap, -num)

        elif op == 'D':
            if not is_empty(nums):
                if num == 1:
                    while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
                        temp = -heapq.heappop(max_heap)
                        if temp in nums:
                            del(nums[temp])
                    nums[-max_heap[0]] -= 1
                else:
                    while min_heap[0] not in nums or nums[min_heap[0]] < 1:
                        temp = heapq.heappop(min_heap)
                        if temp in nums:
                            del(nums[temp])
                    nums[min_heap[0]] -= 1

    if is_empty(nums):
        print('EMPTY')
    else:
        while min_heap[0] not in nums or nums[min_heap[0]] < 1:
            heapq.heappop(min_heap)
        while -max_heap[0] not in nums or nums[-max_heap[0]] < 1:
            heapq.heappop(max_heap)
        print(-max_heap[0], min_heap[0])