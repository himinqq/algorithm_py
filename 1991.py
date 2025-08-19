def preorder(cur):
    print(chr(cur + ord('A') - 1), end='')
    if lc[cur] != 0:
        preorder(lc[cur])
    if rc[cur] != 0:
        preorder(rc[cur])


def inorder(cur):
    if lc[cur] != 0:
        inorder(lc[cur])
    print(chr(cur + ord('A') - 1), end="")
    if rc[cur] != 0:
        inorder(rc[cur])


def postorder(cur):
    if lc[cur] != 0:
        postorder(lc[cur])
    if rc[cur] != 0:
        postorder(rc[cur])
    print(chr(cur + ord('A') - 1),end="")

N = int(input())

lc = [0] * 30
rc = [0] * 30
for _ in range(N):
    c, l, r = input().split()

    # 인덱스 1번부터 N번 까지 사용  (A:1, B:2 ... )
    cur_idx = ord(c) - ord('A') + 1

    if l != '.':
        lc[cur_idx] = ord(l) - ord('A') + 1
    if r != '.':
        rc[cur_idx] = ord(r) - ord('A') + 1

preorder(1)
print()
inorder(1)
print()
postorder(1)
