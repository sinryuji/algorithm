def solution(a, b):
    if b == 1:
        return a
    tmp = solution(a, b // 2) % c
    if b % 2 == 0:
        return tmp * tmp
    else:
        return tmp * tmp * a

a, b, c = map(int, input().split())
print(solution(a, b) % c)