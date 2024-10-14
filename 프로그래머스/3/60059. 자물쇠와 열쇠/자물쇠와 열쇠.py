def turn_right(key, M):
    result = []

    for i in range(M):
        tmp = []
        for j in range(M):
            tmp.append(key[~j][i])
        result.append(tmp)

    return result

def solution(key, lock):
    N, M = len(lock), len(key)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                cnt += 1

    for _ in range(4):
        for i in range(M + N - 1):
            for j in range(M + N - 1):
                tmp = 0
                for x in range(M):
                    for y in range(M):
                        a, b = x - M + 1 + i, y - M + 1 + j
                        if 0 <= a < N and 0 <= b < N:
                            if key[x][y] == 1:
                                if lock[a][b] == 0:
                                    tmp += 1
                                else:
                                    tmp -= 1
                if cnt == tmp:
                    return True
        key = turn_right(key, M)

    return False