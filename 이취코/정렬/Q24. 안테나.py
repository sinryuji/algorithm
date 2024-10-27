# https://www.acmicpc.net/problem/18310

import sys

input = sys.stdin.readline

N = int(input())
houses = sorted(list(map(int, input().split())))

print(houses[(N-1) // 2])
