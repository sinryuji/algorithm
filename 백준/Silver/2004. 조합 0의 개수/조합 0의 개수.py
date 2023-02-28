def count(x, y):
    ret = 0
    while x:
        ret += x // y
        x //= y
    return ret

n, m = map(int, input().split())
two_cnt = count(n, 2) - count(m, 2) - count(n - m, 2)
five_cnt = count(n, 5) - count(m, 5) - count(n - m, 5)
print(min(two_cnt, five_cnt))