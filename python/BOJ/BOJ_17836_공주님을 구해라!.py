# [1] 입력값 설정
from sys import stdin
N, M, T = map(int, stdin.readline().split())
castle = [[] for _ in '_'*N]
for i in range(N):
    castle[i] = list(map(int, stdin.readline().split()))

# [2] bfs 탐색
from collections import deque
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
visited = [[[0]*2 for _ in '_'*M] for _ in  '_'*N] # 3차원 visited

# [2-1] 좌표(i, j), 탐색 시간(n), 검 유무(sword) 4가지 인자로 bfs 탐색
queue = deque([(0, 0, 0, 0)])
visited[0][0][0] = 1
while queue:
    i, j, n, sword = queue.popleft()
    for dr in range(4):
        ni, nj = i+di[dr], j+dj[dr]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj][sword]:
            # [2-2] 검이 없는 상태에서는 칸이 0이나 2일때만 나아간다.
            if not sword:
                if castle[ni][nj] == 0:
                    visited[ni][nj][sword] = n+1
                    queue.append((ni, nj, n+1, sword))
                # [2-3] 2번인 칸을 만나면 sword는 1이 되며, 3차원 visited를 활용한다.
                elif castle[ni][nj] == 2:
                    visited[ni][nj][sword] = n+1
                    visited[ni][nj][1] = n+1
                    queue.append((ni, nj, n+1, 1))
            # [2-4] 검이 있는 상태에서는 아무 칸이나 나아가며, visited[ni][nj][1]에 기록한다.
            elif sword:
                visited[ni][nj][sword] = n+1
                queue.append((ni, nj, n+1, sword))

# [3] 출력 설정
# 검이 있는 상태와 없는 상태의 visited min값을 비교할건데, 값이 0이라면 제외해주어야 하므로 T보다 큰 값을 대입함.
if not visited[N-1][M-1][0]:
    visited[N-1][M-1][0] = T+1
if not visited[N-1][M-1][1]:
    visited[N-1][M-1][1] = T+1
result = min(visited[N-1][M-1][0], visited[N-1][M-1][1])
if result > T:
    print('Fail')
else:
    print(result)