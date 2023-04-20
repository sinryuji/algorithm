l = int(input())
s = input()
r = 31
m = 1234567891
ret = 0

for i in range(l):
    ret += (ord(s[i]) - 96) * (r ** i)
print(ret % m)