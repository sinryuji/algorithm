import sys

input = sys.stdin.readline


def check(arr):
    v, c = 0, 0
    for i in arr:
        if i in vowel:
            v += 1
        else:
            c += 1
    if v >= 1 and c >= 2:
        return True
    return False


def dfs(start, arr):
    if len(arr) == L:
        if check(arr):
            print(''.join(arr))
        return

    for i in range(start, C):
        if arr[-1] < alphas[i]:
            arr.append(alphas[i])
            dfs(start + 1, arr)
            arr.pop()


L, C = map(int, input().split())
alphas = sorted(list(input().split()))
vowel = ['a', 'e', 'i', 'o', 'u']

for i in range(C - L + 1):
    dfs(i + 1, [alphas[i]])