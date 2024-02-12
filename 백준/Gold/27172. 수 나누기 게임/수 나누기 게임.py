from sys import stdin
def main():
    input = stdin.readline
    n = int(input())
    *x, = map(int, input().split())
    max_ = max(x)+1
    a = [False]*max_
    for xi in x:
        a[xi] = True
    ans = [0]*max_
    for xi in x:
        for i in range(xi*2, max_, xi):
            if a[i]:
                ans[xi] += 1
                ans[i] -= 1
    tmp = ''
    for xi in x:
        tmp += str(ans[xi])+' '
    print(tmp)
main()