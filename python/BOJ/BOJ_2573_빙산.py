# [A] delta 방향 설정
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# [B] 빙산이 녹는 melt 함수 설정
def melt():
    global iceberg
    # [B-1] 각 얼음이 얼마나 녹는지를 melting에 저장한 뒤,
    melting = []
    for ice in iceberg:
        [i, j] = ice
        cnt0 = 0
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and not sea[ni][nj]:
                cnt0 += 1
        melting.append(cnt0)

    # [B-2] melting에 저장된 만큼 동시에 녹인다.
    iceberg2 = []
    for n in range(len(melting)):
        [i, j] = iceberg[n]
        rest = sea[i][j] - melting[n]
        if rest > 0:
            sea[i][j] = rest
            iceberg2.append([i, j])
        else:
            sea[i][j] = 0

    # [B-3] 녹고 남은 빙산의 좌표를 갱신해준다.
    iceberg = iceberg2[:]


# [C] BFS 함수 설정
from collections import deque
def bfs(a, b):
    queue = deque([(a, b)])
    visited[a][b] = 1
    while queue:
        i, j = queue.popleft()
        for di, dj in delta:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and sea[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                queue.append((ni, nj))

    return 1

# [1] 입력값 설정
from sys import stdin
N, M = map(int, stdin.readline().split())
sea = [[] for _ in '_'*N]
for i in range(N):
    sea[i] = list(map(int, stdin.readline().split()))

# [1-2] 빙산의 좌표를 iceberg에 저장
iceberg = []
for i in range(N):
    for j in range(M):
        if sea[i][j]:
            iceberg.append([i, j])

# [2] 매년 빙산이 녹는다.
result = 0
while True:
    result += 1
    melt()

    # [2-1] DFS 탐색으로 빙산이 몇 덩어리인지 변수 cnt에 저장
    cnt = 0
    visited = [[0] * M for _ in '_' * N]
    for ice in iceberg:
        [i, j] = ice
        if sea[i][j] and not visited[i][j]:
            cnt += bfs(i, j)

    # [2-2] 빙산이 1덩어리라면 continue, 그렇지 않으면 출력
    if cnt == 1:
        continue
    elif cnt == 0:
        print(0)
        break
    else:
        print(result)
        break