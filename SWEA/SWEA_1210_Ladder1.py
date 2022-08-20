# 입력값 설정
for _ in range(10):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 값이 2인 end_point 찾기
    end_point = 0
    for i in range(100):
        if arr[99][i] == 2:
            end_point = i
            break

    # 밑에서부터 올라오면서 측면이 1일 경우 end_point 이동
    for x in range(99, 0, -1):
        if 0 < end_point < 99:
            if arr[x][end_point - 1] == 1:
                while arr[x][end_point - 1] != 0:
                    end_point += -1
                    if end_point == 0:
                        break

            elif arr[x][end_point + 1] == 1:
                while arr[x][end_point + 1] != 0:
                    end_point += 1
                    if end_point == 99:
                        break

        elif end_point == 0:
            while arr[x][end_point + 1] != 0:
                end_point += 1
                if end_point == 99:
                    break

        elif end_point == 99:
            if arr[x][end_point - 1] == 1:
                while arr[x][end_point - 1] != 0:
                    end_point += -1
                    if end_point == 0:
                        break

    print(f'#{test_case} {end_point}')
