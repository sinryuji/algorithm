def solution(wallpaper):
    row_min = col_min = int(1e9)
    row_max = col_max = 0
    
    for row in range(len(wallpaper)):
        for col in range(len(wallpaper[0])):
            if wallpaper[row][col] == '#':
                row_min = min(row_min, row)
                col_min = min(col_min, col)
                row_max = max(row_max, row)
                col_max = max(col_max, col)

    return [row_min, col_min, row_max + 1, col_max + 1]