from itertools import combinations


def solution(relation):
    row, col = len(relation), len(relation[0])

    combi = []
    for i in range(1, col + 1):
        combi.extend(combinations(range(col), i))

    unique = []
    for i in combi:
        tmp = [tuple(student[key] for key in i) for student in relation]
        print(tmp)
        if len(set(tmp)) == row:
            put = True
            for x in unique:
                if set(x).issubset(i):
                    put = False
                    break
            if put:
                unique.append(i)

    return len(unique)
