def solution(wallpaper):
    row, col = [], []
    
    for r in range(len(wallpaper)):
        for c in range(len(wallpaper[0])):
            if wallpaper[r][c] == '#':
                row.append(r)
                col.append(c)

    return [min(row), min(col), max(row) + 1, max(col) + 1]