i = iter(open(0))
data = list(map(int, i))
print(int(sum(data) / len(data)))
print(sorted(data)[2])