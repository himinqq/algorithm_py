def solution(rows, columns, queries):

    answer = []
    array = [[0 for col in range(columns)] for row in range(rows)]
    t = 1
    for row in range(rows):
        for col in range(columns):
            array[row][col] = t
            t += 1

    for x1,y1,x2,y2 in queries:
        tmp = array[x1-1][y1-1] # 회전 시작 좌표
        mini = tmp # 최솟값 추적
        # 왼 (아래에서 위)
        for k in range(x1-1,x2-1):
            test = array[k+1][y1-1]
            array[k][y1-1] = test
            mini = min(mini, test)

        # 아래 (왼쪽에서 오른쪽)
        for k in range(y1-1,y2-1):
            test = array[x2-1][k+1]
            array[x2-1][k] = test
            mini = min(mini, test)
        # 오른쪽 (아래에서 위)
        for k in range(x2-1,x1-1,-1):
            test = array[k-1][y2-1]
            array[k][y2-1] = test
            mini = min(mini, test)
        # 위 (왼쪽에서 오른쪽)ㅣ
        for k in range(y2-1,y1-1,-1):
            test = array[x1-1][k-1]
            array[x1-1][k] = test
            mini = min(mini, test)

        array[x1-1][y1] = tmp # 원래 맨 처음 왼쪽 위 값(tmp)을 회전 후 빈 공간에 채움
        answer.append(mini)

    return answer