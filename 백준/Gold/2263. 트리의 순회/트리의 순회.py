import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def pre_order(in_s, in_e, post_s, post_e):
    if in_s > in_e or post_s > post_e:
        return

    root = post_order[post_e]
    root_idx = in_order_idx[root]

    left_node_cnt = root_idx - in_s
    right_node_cnt = in_e - root_idx

    print(root, end=' ')
    pre_order(in_s, root_idx - 1, post_s, post_s + left_node_cnt - 1)
    pre_order(root_idx + 1, in_e, post_e - right_node_cnt, post_e - 1)


n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
in_order_idx = [0] * (n + 1)
for i in range(n):
    in_order_idx[in_order[i]] = i

pre_order(0, n - 1, 0, n - 1)