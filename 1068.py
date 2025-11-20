import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
parents = list(map(int, input().split()))
D = int(input())

child = [[] for _ in range(N)]
root = -1
for node,p in enumerate(parents):
    if p != -1:
        child[p].append(node)
    else:
        root = node

def delete_node(cur):
    parents[cur] = -2
    for c in child[cur]:
        delete_node(c)

def count_leaf():
    cnt = 0
    if parents[root] == -2: # 1. 삭제된 노드는 세지 않음
        return 0
    for node in range(N):
        if parents[node] == -2:
            continue

        # 2. 리프 노드인지 확인 : 자식 중 살아남은 노드가 있는지?
        is_leaf = True
        for c in child[node]:
            if parents[c] != -2: # 자식 c 가 삭제되지 않았다면
                is_leaf = False # 리프노드 아님
                break
        if is_leaf:
            cnt += 1
    return cnt

delete_node(D)
print(count_leaf())