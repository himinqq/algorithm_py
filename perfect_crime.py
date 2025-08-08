def dfs(a, b, idx, info, n, m, vis):
    global result
    if idx == len(info):
        if a < n and b < m:
            result = min(result, a)
        return
    if (a, b, idx) not in vis:
        vis.add((a, b, idx))
    else:
        return
    if a >= n or b >= m or a >= result:
        return
    dfs(a + info[idx][0], b, idx + 1, info, n, m, vis)
    dfs(a, b + info[idx][1], idx + 1, info, n, m, vis)


def solution(info, n, m):
    global result
    result = float('inf')
    vis = set()
    dfs(0, 0, 0, info, n, m, vis)
    if result == float('inf'):
        return -1
    else:
        return result
