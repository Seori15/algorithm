# 입력값 설정
for _ in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]

    result = 0
    for i in range(100):

        # case 1. 각 행의 합
        S = 0
        for j in range(100):
            S += arr[i][j]
        if result < S:
            result = S

        # case 2. 각 열의 합
        S = 0
        for j in range(100):
            S += arr[j][i]
        if result < S:
            result = S

        # case 3. 대각선(남동)의 합
        S = 0
        if i + j == 99:
            S += arr[i][j]
            if result < S:
                result = S

    # case 4. 대각선(남서)의 합
    for i in range(100):
        S = 0
        S += arr[i][i]
        if result < S:
            result = S

    print(f'#{T} {result}')