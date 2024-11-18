import itertools

data = [1, 2, 3, 4]

for x in itertools.permutations(data, 3):
    print(*x)
