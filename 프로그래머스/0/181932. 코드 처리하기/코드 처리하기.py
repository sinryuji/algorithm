def solution(code):
    ret = ''
    mode = 0
    for i, c in enumerate(code):
        if mode == 0:
            if c == '1':
                mode = 1
            elif i % 2 == 0:
                ret += c
        else:
            if c == '1':
                mode = 0
            elif i % 2 != 0:
                ret += c
    if not ret:
        ret = "EMPTY"
    return ret