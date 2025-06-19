import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pack, each = zip(*[map(int, input().split()) for _ in range(M)])

mp = min(pack)
me = min(each)

print(min(N // 6 * mp + N % 6 * me, (N // 6 + 1) * mp, N * me))