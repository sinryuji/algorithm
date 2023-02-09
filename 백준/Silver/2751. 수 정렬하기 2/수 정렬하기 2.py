i = iter(open(0))
next(i)
print(*sorted(list(map(int, i))), sep = '\n')