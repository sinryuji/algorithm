import sys

input = sys.stdin.readline


def solve():
    n, p, q = map(int, input().split())

    dp = {0: 1}

    def recur(i):
        nonlocal dp

        ai = dp.get(i, None)
        if ai is not None:
            return ai

        ap = recur(i // p)
        aq = recur(i // q)

        dp[i] = ap + aq

        return ap + aq

    print(recur(n))


if __name__ == "__main__":
    solve()