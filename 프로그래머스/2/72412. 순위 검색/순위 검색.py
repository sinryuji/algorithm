from collections import defaultdict

def bisect_left(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def solution(info, query):
    answer = []

    d = {'java': 'a',
         'cpp': 'b',
         'python': 'c',
         'backend': 'a',
         'frontend': 'b',
         'junior': 'a',
         'senior': 'b',
         'chicken': 'a',
         'pizza': 'b'
         }

    applicants = defaultdict(list)
    for i in info:
        x, y, z, w, s = i.split()
        applicants[d[x] + d[y] + d[z] + d[w]].append(int(s))

    for key in applicants.keys():
        applicants[key].sort()

    def dfs(depth, key):
        nonlocal cnt, s
        if depth == 4:
            arr = applicants[key]
            cnt += len(arr) - bisect_left(arr, s)
            return

        if q[depth] == '-':
            dfs(depth + 1, key + 'a')
            dfs(depth + 1, key + 'b')
            if depth == 0:
                dfs(depth + 1, key + 'c')
        else:
            dfs(depth + 1, key + d[q[depth]])

    for q in query:
        cnt = 0
        x, y, z, w = q.split(' and ')
        f, s = w.split()
        q, s = [x, y, z, f], int(s)
        dfs(0, '')
        answer.append(cnt)

    return answer
