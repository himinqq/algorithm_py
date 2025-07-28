def hanoi(start, end, extra, n, ans):
    if n == 1:
        ans.append([start, end])
    else:
        hanoi(start,extra,end,n-1,ans)
        hanoi(start,end,extra,1,ans)
        hanoi(extra,end,start,n-1,ans)
    return ans

def solution(n):
    answer = []
    hanoi(1,3,2,n,answer)
    return answer
