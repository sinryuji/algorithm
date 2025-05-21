import sys

input = sys.stdin.readline

N = int(input())
K = int(input())
sensor = sorted(list(map(int, input().split())))
diff = sorted([sensor[i] - sensor[i-1] for i in range(1, N)], reverse = True)

print(sum(diff[K-1:]))