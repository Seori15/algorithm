# dfs 함수 설정
def dfs(x, y, dr):
    global x1, y1, result

    # 종료 조건. 한 바퀴 돌아서 자기 위치로 왔을 때, 디저트 종류합을 비교한다.
    if dr == 3 and (x, y) == (x1, y1):
        if result < sum(desserted):
            result = sum(desserted)
        return

    # 반복 내용. x,y 방문처리 한 후 다음 지점을 bfs한다.
    if not desserted[cafe[x][y]]:
        desserted[cafe[x][y]] = 1

        if 0 <= x+dx[dr] < N and 0 <= y+dy[dr] < N and dr <= 3:
            dfs(x+dx[dr], y+dy[dr], dr)         # 방향 그대로 진행

        if dr <= 2 and 0 <= x+dx[dr+1] < N and 0 <= y+dy[dr+1] < N:
            dfs(x+dx[dr+1], y+dy[dr+1], dr+1)   # 방향 꺾어서 진행

        desserted[cafe[x][y]] = 0
    else:   # 디저트의 종류가 겹친다면 그만 탐색
        return


# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in '_'*N]
    dx = [-1, 1, 1, -1]
    dy = [1, 1, -1, -1] # 1 5 7 11시 순서
    result = -1
    desserted = [0] * 101
    for i in range(1, N-1):
        for j in range(N-2):
            x1, y1 = i, j
            dfs(i, j, 0)

    print(f'#{test_case} {result}')