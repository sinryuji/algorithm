import sys
sys.setrecursionlimit(int(1e9))

lines = sys.stdin.readlines()

tree = []
for line in lines:
    tree.append(int(line))

def solution(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start+1, end+1):
        if tree[i] > tree[start]:
            mid = i
            break
    solution(start+1, mid-1)
    solution(mid, end)
    print(tree[start])

solution(0, len(tree)-1)