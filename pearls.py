def solution(sequence):
    a = [0]
    b = [0]
    for i in range(len(sequence)):
        num = sequence[i]
        if i % 2 == 0:
            a.append(num)
            b.append(num*-1)
        else:
            b.append(num)
            a.append(num*-1)
    print(a)
    print(b)
    def dp(arr):
        for i in range(1,len(arr)):
            arr[i] = max(arr[i], arr[i-1]+arr[i])
        return arr

    return max(max(dp(a)),max(dp(b)))