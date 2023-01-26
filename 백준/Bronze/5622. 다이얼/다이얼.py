dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
ret = 0;
for c in input():
    for i in dial:
        if c in i:
            ret += dial.index(i) + 3
print(ret)