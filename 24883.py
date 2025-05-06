import sys

def is_repeat(num: int):
    target = str(num)
    chk = set()
    for i in target:
        chk.add(i)
    if len(chk) != len(target):
        return False
    return True

while True:
    line = sys.stdin.readline().strip() #더이상 읽을 라인 없으면 빈 문자열 반환
    if line == "": break
    n, m = map(int, line.split())
    ans = 0
    for num in range(n, m+1):
        if is_repeat(num):
            ans += 1
    print(ans)