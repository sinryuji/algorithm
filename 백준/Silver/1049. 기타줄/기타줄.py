import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pack, each = zip(*[map(int, input().split()) for _ in range(M)])

min_pack = min(pack)
min_each = min(each)

print(min(N // 6 * min_pack + N % 6 * min_each, (N // 6 + 1) * min_pack, N * min_each))