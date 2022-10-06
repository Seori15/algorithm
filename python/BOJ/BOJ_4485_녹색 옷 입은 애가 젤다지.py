di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1] # 12시부터 시계방향

# dijkstra 함수 설정
def dijkstra(a, b):
    key[a][b] = cave[a][b]
    while True:
        # 1. 가장 key값이 작은 지점을 선택
        minV = INF
        for i in range(N):
            for j in range(N):
                if minV > key[i][j] and not visited[i][j]:
                    minV = key[i][j]
                    ti, tj = i, j

        # 종료조건. N-1, N-1지점에 도달
        if (ti, tj) == (N-1, N-1):
            return key[ti][tj]

        # 2. 선택 지점 visited처리 후 주변 지점 key값 갱신
        visited[ti][tj] = 1
        for dr in range(4):
            ni, nj = ti+di[dr], tj+dj[dr]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                key[ni][nj] = min(key[ni][nj], key[ti][tj] + cave[ni][nj])

# 입력값 설정
from sys import stdin
T = 0
while True:
    N = int(stdin.readline())
    if N == 0:
        break
    T += 1
    cave = [[] for _ in '_'*N]
    for i in range(N):
        cave[i] = list(map(int, stdin.readline().split()))

    INF = 10*N**2
    key = [[INF]*N for _ in '_'*N]
    visited = [[0]*N for _ in '_'*N]
    print(f'Problem {T}: {dijkstra(0, 0)}')