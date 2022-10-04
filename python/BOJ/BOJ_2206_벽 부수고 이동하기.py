di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

# bfs 함수 설정
def bfs(a, b, punch):
    global result
    visited[a][b][punch] = 1
    queue = [(a, b, punch)]
    while queue:
        L = len(queue)
        q2 = []
        for n in range(L):
            i, j, punch = queue[n]
            # 좌표에 도달했다면 result값 반영
            if i == N-1 and j == M-1:
                result = visited[i][j][punch]
                return
            for dr in range(4):
                ni, nj = i+di[dr], j+dj[dr]
                if 0 <= ni < N and 0 <= nj < M and visited[ni][nj][punch] == 0:
                    # 벽이 아니라면 그냥 이동
                    if arr[ni][nj] == 0:
                        visited[ni][nj][punch] = visited[i][j][punch] + 1
                        q2.append((ni, nj, punch))
                    # 벽을 부수지 않았으며 벽을 만났다면 부수고 이동
                    if punch == 0 and arr[ni][nj] == 1:
                        visited[ni][nj][1] = visited[i][j][punch] + 1
                        q2.append((ni, nj, 1))
        queue = q2[:]


# 입력값 설정
N, M = map(int, input().split())
arr = [[] for _ in '_'*N]
for i in range(N):
    arr[i] = list(map(int, list(input())))

visited = [[[0]*2 for _ in '_'*M] for _ in '_'*N]
result = -1
bfs(0, 0, 0)

print(result)
