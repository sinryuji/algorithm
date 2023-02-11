import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
sortedArr = sorted(list(set(arr)))
dict = {x : i for i, x in enumerate(sortedArr)}
sys.stdout.write(" ".join([str(dict[i]) for i in arr]))