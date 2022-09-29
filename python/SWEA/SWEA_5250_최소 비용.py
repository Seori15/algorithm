# bfs 풀이
# bfs 함수 설정. 초기값을 queue에 넣고 4방향 탐색을 돌린다.
# result라는 리스트에 연료값을 최소값으로 갱신한다.
def bfs(a, b):
    queue = [(a, b)]
    while queue:
        i, j = queue.pop(0)
        for dr in range(4):
            ni, nj = i+di[dr], j+dj[dr]
            if 0 <= ni < N and 0 <= nj < N:
                fuel = result[i][j] + 1
                if height[i][j] < height[ni][nj]:
                    fuel += height[ni][nj] - height[i][j]
                if result[ni][nj] == 0 or result[ni][nj] > fuel:
                    result[ni][nj] = fuel
                    queue.append((ni, nj))

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    height = [[]*N for _ in '_'*N]
    result = [[0]*N for _ in '_'*N]
    for i in range(N):
        height[i] = list(map(int, input().split()))
    bfs(0, 0)
    print(f'#{test_case} {result[N-1][N-1]}')


------------------------------------------------------
# dijkstra 풀이
# dijkstra 함수 설정
def dijkstra(a, b):
    # 초기값 a, b는 visited 처리 및 result 0 처리 해준다.
    queue = [(a, b)]
    result[a][b] = 0
    visited[a][b] = 1

    # queue에 우리가 원하는 좌표가 들어올 때까지 반복한다. ※ 꼭 queue일 필요 없다.
    while (N-1, N-1) not in queue:
        minV = INF

        # queue에 존재하는 모든 좌표에 대해서, 상하좌우 값을 비교하고, visited하지 않은 최소값 좌표를 구한다.
        for (i, j) in queue:
            for dr in range(4):
                ni, nj = i+di[dr], j+dj[dr]
                if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                    if height[i][j] < height[ni][nj]:
                        result[ni][nj] = min(result[ni][nj], result[i][j] + height[ni][nj] - height[i][j] + 1)
                    else:
                        result[ni][nj] = min(result[ni][nj], result[i][j] + 1)

                    if minV > result[ni][nj]:
                        minV = result[ni][nj]
                        c, d = ni, nj

        # 구한 최소값 좌표를 queue에 append하면서 visited처리 후 반복.
        visited[c][d] = 1
        queue.append((c, d))


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
INF = 1000000000000000
# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    height = [[] for _ in '_'*N]
    result = [[INF]*N for _ in '_'*N]
    visited = [[0]*N for _ in '_'*N]
    for i in range(N):
        height[i] = list(map(int, input().split()))
    dijkstra(0, 0)
    print(f'#{test_case} {result[N-1][N-1]}')


------------------------------------------------------
# dijkstra 풀이(교수님 ver.)
# dijkstra 함수 설정
def dijkstra(a, b):
    # 초기값 a, b는 visited 처리 및 result 0 처리 해준다.
    result[a][b] = 0
    for _ in range(N*N): # 출발점을 제외한 총 N^2-1개의 지점 값을 갱신해줘야 한다.
        # 배열에서 가장 작은 minV값과 index를 찾는다.
        minV = INF
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0 and minV > result[i][j]:
                    minV = result[i][j]
                    wi, wj = i, j

        # 찾은 index를 visited 처리 후 인접한 result 값을 갱신한다.
        visited[wi][wj] = 1
        for dr in range(4):
            ni, nj = wi+di[dr], wj+dj[dr]
            if 0 <= ni < N and 0 <= nj < N:
                if height[wi][wj] < height[ni][nj]:
                    result[ni][nj] = min(result[ni][nj], result[wi][wj] + height[ni][nj] - height[wi][wj] + 1)
                else:
                    result[ni][nj] = min(result[ni][nj], result[wi][wj] + 1)

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
INF = 1000000000000000
# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    height = [[] for _ in '_'*N]
    result = [[INF]*N for _ in '_'*N]
    visited = [[0]*N for _ in '_'*N]
    for i in range(N):
        height[i] = tuple(map(int, input().split()))
    dijkstra(0, 0)
    print(f'#{test_case} {result[N-1][N-1]}')