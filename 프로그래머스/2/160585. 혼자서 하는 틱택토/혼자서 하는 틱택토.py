def solution(board):
    n, m = len(board), len(board[0])
    o, x = 0, 0
    win = []
    
    for row in range(n):
        if board[row] == 'XXX' or board[row] == 'OOO':
            win.append(board[row])
        for col in range(m):
            if board[row][col] == 'X':
                x += 1
            elif board[row][col] == 'O':
                o += 1
                
    for col in range(m):
        a = board[0][col] + board[1][col] + board[2][col]
        if a == 'XXX' or a == 'OOO':
            win.append(a)
    
    a = board[0][0] + board[1][1] + board[2][2]
    if a == 'XXX' or a == 'OOO':
        win.append(a)
        
    a = board[0][2] + board[1][1] + board[2][0]
    if a == 'XXX' or a == 'OOO':
        win.append(a)     
    
    flag = False
    if len(win) == 0:
        flag = True
    if len(win) == 1:
        if win[0] == 'OOO':
            if o - x == 1:
                flag = True
        if win[0] == 'XXX':
            if o == x:
                flag = True
    if len(win) == 2 and win[0] == 'OOO' and win[1] == 'OOO':
        if o == 5 and x == 4:
            flag = True
    
    return 0 if o - x < 0 or o - x > 1 or not flag else 1