# [A] 상하좌우 방향 delta 설정
delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# [B] bfs 함수 설정
from collections import deque

def bfs(a, b):
    queue = deque([(K, a, b)])
    visited[K][a][b] = 1
    while queue:
        spell, i, j = queue.popleft()
        if (i, j) == (N - 1, M - 1):
            return visited[spell][i][j]

        for di, dj in delta:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[spell][ni][nj]:
                if arr[ni][nj] == 0:
                    visited[spell][ni][nj] = visited[spell][i][j] + 1
                    queue.append((spell, ni, nj))
                elif spell and arr[ni][nj] == 1 and not visited[spell-1][ni][nj]:
                    visited[spell-1][ni][nj] = visited[spell][i][j] + 1
                    queue.append((spell-1, ni, nj))

    return -1

# [1] 입력값 설정
from sys import stdin
N, M, K = map(int, stdin.readline().split())
arr = [[] for _ in '_'*N]
for i in range(N):
    arr[i] = list(map(int, list(input())))

# [2] bfs 탐색
result = 0
visited = [[[0]*M for _ in '_'*N] for _ in '_'*(K+1)]
print(bfs(0, 0))
