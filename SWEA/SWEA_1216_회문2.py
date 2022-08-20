# 입력값 설정
for test_case in range(1, 11):
    T = int(input())
    arr = [input() for i in range(100)]

# M이 100부터 1씩 줄어가며 회문검사
    result = 0
    for M in range(100, 0, -1):
        for i in range(100):
            for j in range(100 - M + 1):

# X방향 회문체크
                if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                    result = M
                    break

# Y방향 회문체크
                test_y = []
                for k in range(M):
                    test_y.append(arr[j+k][i])
                if test_y == test_y[::-1]:
                    result = M
                    break
            if result == M:
                break
        if result == M:
            break

    print(f'#{test_case} {result}')