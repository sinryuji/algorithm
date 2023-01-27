croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
str = input()
for c in croatia:
    str = str.replace(c, '.')
print(len(str))