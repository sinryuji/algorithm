def solution(rows, columns, queries):
    answer = []

    matrix = [[i * columns + 1 + j for j in range(columns)] for i in range(rows)]

    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        tmp = [row[:] for row in matrix]
        arr = []
        for y in range(y1 + 1, y2 + 1):
            tmp[x1][y] = matrix[x1][y - 1]
            arr.append(tmp[x1][y])
        for x in range(x1 + 1, x2 + 1):
            tmp[x][y2] = matrix[x - 1][y2]
            arr.append(tmp[x][y2])
        for y in range(y2 - 1, y1 - 1, -1):
            tmp[x2][y] = matrix[x2][y + 1]
            arr.append(tmp[x2][y])
        for x in range(x2 - 1, x1 - 1, -1):
            tmp[x][y1] = matrix[x + 1][y1]
            arr.append(tmp[x][y1])
        matrix = tmp
        answer.append(min(arr))

    return answer
