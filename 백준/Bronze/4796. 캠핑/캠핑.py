import sys

input = sys.stdin.readline

count = 0
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break

    count += 1
    print(f'Case {count}: {V // P * L + (L if V % P > L else V % P)}')