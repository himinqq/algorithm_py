import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0] * m
used = [False] * (n + 1)

def func(k): #현재 k까지 수 택한 상태에서 arr[k] 정하는 함수
    if k == m: #m개를 모두 택했으면
        print(*arr) #arr에 기록해둔 수 출력
        return
    for i in range(1, n + 1): #1~n까지의 수 확인하며 아직 쓰이지 않은 수 찾기
        if not used[i]: #아직 i가 사용되지 않았으면
            arr[k] = i #k번째 수를 i로 정함
            used[i] = True #i를 사용되었다고 표시
            # arr[k]=i로 둔 상태에서 func(k+1)에 들어갔다가 모든 과정 끝난 것
            #다음 수를 정하러 한 단계 더 들어감
            func(k + 1)

            used[i] = False #// k번째 수를 i로 정한 모든 경우에 대해 다 확인했으니 i를 이제 사용되지않았다고 명시함.

func(0)
