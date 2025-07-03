# 순서 바꾸지 않고 더하거나 빼서 타겟 만들기

def dfs(numbers, target, depth, total):
    if depth == len(numbers): # 각 리프노드에서 target 과 같으면 1 아니면 0
        return 1 if target == total else 0
    return ( # +인 경우와 -인 경우 나눠서 재귀호출
            dfs(numbers, target, depth + 1, total + numbers[depth]) +
            dfs(numbers, target, depth + 1, total - numbers[depth])
    )


def solution(numbers, target):
    return dfs(numbers, target, 0, 0)
