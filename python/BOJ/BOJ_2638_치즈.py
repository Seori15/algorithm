from collections import deque

# [A] delta 설정
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

# [B] 공기면(0,0)과 닿아있는 지 visited에 작성하는 air_check 함수 설정
def air_check(a, b):
    queue = deque([(a, b)])
    while queue:
        i, j = queue.popleft()
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and table[ni][nj] == 0 and not visited[ni][nj]:
                visited[ni][nj] = 1
                queue.append((ni, nj))

# [C] 치즈의 4방향이 공기와 맞닿는지 확인하는 check 함수 설정
def check(i, j):
    contact = 0
    for di, dj in delta:
        ni, nj = i+di, j+dj
        if visited[ni][nj]:
            contact += 1

    if contact > 1:
        melt.append((i, j))


# [1] 입력값 설정
N, M = map(int, input().split())
table = [[] for _ in '_'*N]
for i in range(N):
    table[i] = list(map(int, input().split()))

# [2] 치즈의 좌표를 cheese 리스트에 저장한다.
cheese = []
for i in range(N):
    for j in range(M):
        if table[i][j] == 1:
            cheese.append((i, j))

# [3] while문을 통해 치즈가 녹는 시간 result를 계산할 것이다.
result = 0
while cheese:
    # [3-1] 빈 리스트 visited를 작성하고, air_check 함수를 통해 공기면(0,0)과 닿아있는지를 작성한다.
    visited = [[0]*M for _ in '_'*N]
    air_check(0, 0)

    # [3-2] check 함수로 공기와 2면이 맞닿아 있는, 녹을 치즈를 선별하여 melt 리스트에 넣는다.
    melt = []
    for (i, j) in cheese:
        check(i, j)

    # [3-3] 녹을 melt 치즈를 cheese 리스트와 table에서 없앤다.
    for (i, j) in melt:
        cheese.remove((i, j))
        table[i][j] = 0

    result += 1

print(result)
