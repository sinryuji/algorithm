import sys

input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)])

tri = arr[:3]
ans = sum(tri) if tri[2] < tri[0] + tri[1] else -1
for length in arr[3:]:
    tri.pop(0)
    tri.append(length)
    if tri[2] < tri[0] + tri[1]:
        ans = sum(tri)

print(ans)