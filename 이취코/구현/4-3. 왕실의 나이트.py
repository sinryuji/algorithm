location = input()
col = ord(location[0]) - ord('a') + 1
row = int(location[1])
move = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
cnt = 0
for i in move:
    tmpCol = col + i[0]
    tmpRow = row + i[1]
    if tmpCol < 1 or tmpCol > 8 or tmpRow < 1 or tmpRow > 8:
        continue
    cnt += 1
print(cnt)
