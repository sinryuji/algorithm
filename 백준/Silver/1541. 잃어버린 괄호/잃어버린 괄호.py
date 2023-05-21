exp = list(input().split('-'))
exp2 = []
for i in exp:
    if '+' in i:
        exp2.append(sum(map(int, i.split('+'))))
    else:
        exp2.append(int(i))
        
ret = exp2[0]
for i in exp2[1:]:
    ret -= i
    
print(ret)