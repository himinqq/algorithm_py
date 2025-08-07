def solution(n, info):
    global ans, max_diff

    def diff(ryan):
        s = 0
        for i in range(11):
            if ryan[i] == info[i] == 0:
                continue
            if ryan[i] > info[i]:
                s += 10 - i
            else:
                s -= 10 - i
        return s

    def dfs(idx, left, ryan):
        global ans, max_diff
        if idx == -1 and left:
            return
        if left == 0:
            d = diff(ryan)
            if max_diff < d:
                ans = ryan[:]
                max_diff = d
            return

        for i in range(left, -1, -1):
            ryan[idx] = i
            dfs(idx - 1, left - i, ryan)
            ryan[idx] = 0
    ans = [0 for _ in range(11)]
    max_diff = 0
    dfs(10,n,[0 for _ in range(11)])

    return ans if max_diff != 0 else[-1]
