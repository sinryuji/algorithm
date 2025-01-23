def solution(mats, park):
    answer = -1
    
    def check(r, c, size):
        if r + size >= row or c + size >= col:
            return False
        for y in range(r, r + size + 1):
            for x in range(c, c + size + 1):
                if park[y][x] != '-1':
                    return False
        return True
    
    row, col = len(park), len(park[0])
    max_size = 0
    for r in range(row):
        for c in range(col):
            size = 1
            while check(r, c, size):
                size += 1
            max_size = max(max_size, size)
            
    mats.sort()
    for mat in mats:
        if mat > max_size:
            break
        answer = mat
    
    return answer