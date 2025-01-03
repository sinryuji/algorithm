def solution(users, emoticons):
    answer = [0, 0]

    def cal(sales):
        nonlocal answer
        res = [0, 0]
        for user in users:
            s = 0
            for i in range(len(sales)):
                if sales[i] >= user[0]:
                    s += emoticons[i] - (emoticons[i] * sales[i] // 100)
            if s >= user[1]:
                res[0] += 1
            else:
                res[1] += s
        answer = max(answer, res)

    def dfs(sales, m):
        if len(sales) == m:
            cal(sales)
            return

        for i in [10, 20, 30, 40]:
            sales.append(i)
            dfs(sales, m)
            sales.pop()

    dfs([], len(emoticons))

    return answer
