def solution(user_id, banned_id):
    def match(user, ban):
        if len(user) != len(ban):
            return False
        for i in range(len(user)):
            if ban[i] != '*' and ban[i] != user[i]:
                return False
        return True

    result = set()

    # ban 기준으로 모든 user 를 탐색
    def dfs(idx, path):
        if idx == len(user_id):
            result.add(tuple(sorted(path)))
            return
        for user in user_id:
            if user not in path and match(user, banned_id[idx]):
                dfs(idx + 1, path + [user])

    dfs(0, [])

    return len(result)
