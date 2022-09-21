# 입력값 설정
N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in '_'*N]

clear_area = [[0]*M for _ in '_'*N]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1] # 북 동 남 서

# 로봇 작동 설정
# 1. 현재 위치를 청소한다.
while True:
    if not clear_area[r][c]:
        clear_area[r][c] = 1

    # 2. 현재 방향을 기준으로 왼쪽부터 차례대로 탐색을 진행한다.
    # 2-1. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 전진하고 1번으로
    turn = 0
    while turn != 4:
        d = (d-1)%4
        i, j = r+dx[d], c+dy[d]
        # if 0 <= i < N and 0 <= j < M:
        if not clear_area[i][j] and arr[i][j] == 0:
            r, c = i, j
            break
        # 2-2. 왼쪽 방향에 청소할 공간이 없다면, 회전만 하고 다시 2번을 반복
        else:
            turn += 1
            continue

    # 2-1에서 1번으로 돌아가기 위한 조건
    if turn != 4:
        continue
    # 2-3. 네 방향 모두 청소가 이미 되어있거나 벽인 경우 후진하고 2번으로 돌아간다.
    else:
        i, j = r+dx[(d-2)%4], c+dy[(d-2)%4]
        # if 0 <= i < N and 0 <= j < M:
        if arr[i][j] == 0:
            r, c = i, j
            # 2-4. 후진도 할 수 없으면 작동을 멈춘다.
        else:
            break

# 청소한 clear_area 합계 출력
result = 0
for i in range(1, N-1):
    result += sum(clear_area[i])

print(result)