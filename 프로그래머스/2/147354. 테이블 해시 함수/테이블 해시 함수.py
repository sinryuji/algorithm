def solution(data, col, row_begin, row_end):
    answer = 0

    data.sort(key=lambda x: (x[col - 1], -x[0]))

    s = []
    for i in range(row_begin - 1, row_end):
        s.append(sum(n % (i+1) for n in data[i]))

    answer = s[0]
    for n in s[1:]:
        answer ^= n

    return answer