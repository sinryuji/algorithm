str = input().upper()
max_cnt = 0
for i in range(26):
    cnt = str.count(chr(i + 65))
    if max_cnt < cnt:
        max_cnt = cnt
        max_chr = chr(i + 65)
    elif max_cnt == cnt:
        max_chr = '?'
print(max_chr)