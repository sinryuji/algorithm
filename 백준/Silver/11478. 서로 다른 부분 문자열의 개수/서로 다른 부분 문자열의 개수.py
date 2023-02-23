str = input()
s = set()
for i in range(len(str)):
    for j in range(len(str)):
        s.add(str[j:j+i])
print(len(s))