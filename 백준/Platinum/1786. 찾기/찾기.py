def kmp_table(pattern):
    table = [0] * len(pattern)

    pidx = 0
    for idx in range(1, len(pattern)):
        while pidx > 0 and pattern[idx] != pattern[pidx]:
            pidx = table[pidx - 1]

        if pattern[idx] == pattern[pidx]:
            pidx += 1
            table[idx] = pidx

    return table


def kmp(word, pattern):
    table = kmp_table(pattern)

    results = []
    pidx = 0
    for idx in range(len(word)):
        while pidx > 0 and word[idx] != pattern[pidx]:
            pidx = table[pidx - 1]

        if word[idx] == pattern[pidx]:
            if pidx == len(pattern) - 1:
                results.append(idx - len(pattern) + 2)
                pidx = table[pidx]
            else:
                pidx += 1

    return results


T = input()
P = input()

answer = kmp(T, P)
print(len(answer))
print(*answer)
