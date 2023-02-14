import sys

n = int(sys.stdin.readline())
person = [list(map(int, i.split())) for i in sys.stdin.readlines()]
for i in range(n):
    rank = 1
    for j in range(n):
        if i != j and person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            rank += 1
    sys.stdout.write(str(rank) + ' ')