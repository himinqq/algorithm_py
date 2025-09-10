def solution(s):
    answer = 0

    N = len(s)
    for i in range(N):
        for j in range(i+1,N+1):
            if s[i:j] == s[i:j][::-1]:
                answer = max(answer,len(s[i:j]))

    return answer