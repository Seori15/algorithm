# dijkstra 함수 설정
def dijkstra(a, b):
    global result
    key[a][b] = 0
    for _ in range(N*N):
        # key값이 제일 작은 (i, j)를 찾고
        minV = INF
        for i in range(N):
            for j in range(N):
                if not visited[i][j] and minV > key[i][j]:
                    minV = key[i][j]
                    ti, tj = i, j

        # 찾은 (i, j)의 상하좌우 (ni, nj) key값들을 갱신해준다.
        visited[ti][tj] = 1
        for dr in range(4):
            ni, nj = ti + di[dr], tj + dj[dr]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                key[ni][nj] = min(key[ni][nj], key[ti][tj] + arr[ni][nj])

    return key[N-1][N-1]

# 입력값 설정
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
INF = 1000000

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in '_'*N]
    key = [[INF]*N for _ in '_'*N]
    visited = [[0]*N for _ in '_'*N]
    result = 0
    print(f'#{test_case} {dijkstra(0, 0)}')
