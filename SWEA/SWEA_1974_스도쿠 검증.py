# 입력값 설정하기
T = int(input())
for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1

# 가로줄 검증
    for i in range(9):
        checklist1 = set(arr[i])
        if len(checklist1) != 9:
            result = 0
            break

# 세로줄 검증
        templist2 = []
        for j in range(9):
            templist2.append(arr[j][i])
        checklist2 = set(templist2)
        if len(checklist2) != 9:
            result = 0
            break

# 3x3 칸 검증
        dx = [0, 3, 3, -6, 3, 3, -6, 3, 3]
        dy = [0, 0, 0, 3, 0, 0, 3, 0, 0]
        x1, x2 = dx[i], 3 + dx[i]
        y1, y2 = dy[i], 3 + dy[i]
        templist3 = []
        for x in range(x1, x2):
            for y in range(y1, y2):
                templist3.append(arr[x][y])
        checklist3 = set(templist3)
        if len(checklist3) != 9:
            result = 0
            break


    print(f'#{test_case} {result}')