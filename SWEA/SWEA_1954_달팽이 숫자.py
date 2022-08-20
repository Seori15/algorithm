# 입력값 설정하기
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    di = [0, 1, 0, -1] # 달팽이 움직임 순서대로 설정
    dj = [1, 0, -1, 0]
    count = 1
    i, j = 0, 0
    index = 0

# N^2만큼 숫자를 입력하며 달팽이 그리기
    while count <= N**2:

        arr[i][j] = count
        ni, nj = i + di[index % 4], j + dj[index % 4]
        if ni < N and nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
        else:
            index += 1
            i += di[index % 4]
            j += dj[index % 4]
        count += 1

    print(f'#{test_case}')
    for i in range(N):
        for j in arr[i]:
            print(j, end = ' ')
        print()