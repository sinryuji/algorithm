import sys

input = sys.stdin.readline


def bs(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return right + 1


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


N, M, K = map(int, input().split())
cards = sorted(list(map(int, input().split())))
cheolsu = list(map(int, input().split()))

parent = [i for i in range(N + 1)]

# answer = [[] for _ in range(N + 1)]

for i in cheolsu:
    root = find(i)
    idx = bs(cards, root)
    parent[i] = cards[idx]
    print(cards[idx])
    # answer[i].append(cards[idx])

# for i in set(cheolsu):
#     print(*answer[i], sep='\n')
