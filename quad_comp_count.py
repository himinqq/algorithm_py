def quad(arr, x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if (arr[i][j] != arr[x][y]): #구역 내 어떤 원소라도 x,y와 다르면 4등분 후 재귀호출
                n //= 2
                quad(arr, x, y, n) #왼쪽 위
                quad(arr, x + n, y, n) #왼쪽 아래
                quad(arr, x, y + n, n) #오른쪽 위
                quad(arr, x + n, y + n, n) #오른쪽 아래
                return
    # 모든 값이 같다면 압축 가능 > 해당값의 개수를 하나 추가
    answer[arr[x][y]] += 1


def solution(arr):
    global answer
    answer = [0, 0]
    quad(arr, 0, 0, len(arr))

    return answer
