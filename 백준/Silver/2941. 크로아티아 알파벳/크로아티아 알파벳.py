croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
str = input()
ret = 0
for c in croatia:
    ret += str.count(c)
    str = str.replace(c, '.')
str = str.replace('.', '')
print(ret + len(str))