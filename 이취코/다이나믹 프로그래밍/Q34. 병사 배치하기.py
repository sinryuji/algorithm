# https://www.acmicpc.net/problem/18353

import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))

###### 이진 탐색을 이용하여 원소가 들어갈 적절한 위치를 찾는 풀이 #####
# import sys
#
# input = sys.stdin.readline
#
#
# def bs(array, target):
#     left, right = 0, len(array) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] > target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return left
#
#
# N = int(input())
# arr = list(map(int, input().split()))
# s = [arr[0]]
#
# for i in arr[1:]:
#     if i < s[-1]:
#         s.append(i)
#     else:
#         s[bs(s, i)] = i
#
# print(N - len(s))
