import sys

input = sys.stdin.readline


def solve():
    x, y = map(int, input().split())
    dist = y - x

    if dist == 1 or dist == 2:
        return dist

    cd = 2
    end = 4
    answer = 3

    while dist > end:
        answer += 1
        end += cd
        if answer % 2 == 0:
            cd += 1

    return answer


T = int(input())
for _ in range(T):
    print(solve())