import sys

input = sys.stdin.readline

N = int(input())
result = set()
number = []


def dfs():
    if number:
        result.add(int(''.join(map(str, number))))
    for i in range(10):
        if not number or number[-1] > i:
            number.append(i)
            dfs()
            number.pop()


dfs()
result = sorted(result)
print(result[N - 1] if len(result) >= N else -1)