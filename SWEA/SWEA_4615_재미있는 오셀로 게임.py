# 입력값 설정
T = int(input())
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
direction = [0, 1, 2, 3, 4, 5, 6, 7] # 12시부터 시계방향
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    # 게임판 시작 돌 배치
    arr = [[0]*N for _ in '_'*N]
    arr[(N//2)-1][(N//2)-1], arr[N//2][N//2] = 2, 2
    arr[(N//2)-1][N//2], arr[N//2][(N//2)-1] = 1, 1

    # 수 입력 설정
    for i in range(M):
        y, x, color = map(int, input().split())
        y, x = y-1, x-1
        arr[x][y] = color

        # 오셀로 룰 설정. 12시부터 차례대로 탐색한다
        for dr in direction:
            idx = []
            for n in range(1, N):
                # 탐색하는데 보드판 범위 내이고 다른 색 돌이라면 index를 저장한다.
                if 0 <= x + n*dx[dr] < N and 0 <= y + n*dy[dr] < N and arr[x+n*dx[dr]][y+n*dy[dr]] == 3-color:
                    idx.append([x + n * dx[dr], y + n * dy[dr]])
                    if 0 <= x + (n+1) * dx[dr] < N and 0 <= y + (n+1)*dy[dr] < N: # 다음 돌도 보드판 범위일 때,
                        if arr[x+(n+1)*dx[dr]][y+(n+1)*dy[dr]] == 3-color: # 그 다음 돌도 다른 색이라면 continue
                            continue
                        elif arr[x+(n+1)*dx[dr]][y+(n+1)*dy[dr]] == color: # 그 다음 돌이 같은 색이라면 index 저장된 돌의 색을 뒤집는다.
                            for a, b in idx:
                                arr[a][b] = color
                        else: # 다음 돌이 0이라면 break하고 다음 방향 탐색
                            break
                    else: # 보드판 범위를 벗어난다면 break
                        break
                else: # 보드판 범위를 벗어난다면 break하고 다음 방향 탐색
                    break

    # 출력값 설정. 흑돌과 백돌의 개수를 센다
    cntB, cntW = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                cntB += 1
            elif arr[i][j] == 2:
                cntW += 1

    print(f'#{test_case} {cntB} {cntW}')