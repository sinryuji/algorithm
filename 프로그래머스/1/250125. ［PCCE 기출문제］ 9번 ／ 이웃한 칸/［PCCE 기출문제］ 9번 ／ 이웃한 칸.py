def solution(board, h, w):
    answer = 0
    
    target = board[h][w]
    n = len(board)
    dw = [1, -1, 0, 0]
    dh = [0, 0, 1, -1]
    for i in range(4):
        nw, nh = dw[i] + w, dh[i] + h
        if (0 <= nw < n and 0 <= nh < n and board[nh][nw] == target):
            answer += 1
    
    return answer