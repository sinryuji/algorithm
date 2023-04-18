n = int(input())
a = list(map(int, input().split()))
s = [a[0]]

for i in a[1:]:
    if s[-1] < i:
        s.append(i)
    else:
        for j,v in enumerate(s):
            if i <= v:
                s[j] = i
                break
print(len(s))