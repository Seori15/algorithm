# 0. BFS 함수 설정
def BFS(a, b):
    visited[a][b] = 1
    queue = [[a, b]]

    # queue에서 deque하면서 탐색을 반복한다.
    while True:
        [i, j] = queue.pop(0)

        # ni와 nj가 범위 내에 있으며, 방문하지 않았고 벽이 아니라면 queue에 추가
        for n in range(4):
            ni, nj = i+di[n], j+dj[n]
            if 0 <= ni < N and 0 <= nj < N:
                if not visited[ni][nj] and maze[ni][nj] != 1:
                    visited[ni][nj] = visited[i][j] + 1
                    queue.append([ni, nj])

        if maze[i][j] == 3:     # 미로에서 도착점을 만나면 visited-2를 반환
            return visited[i][j]-2

        if len(queue) == 0:     # 도착점을 찾지 못하면 0을 반환
            return 0

# 1. 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    dj = [1, -1, 0, 0]
    di = [0, 0, -1, 1]
    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                a, b = i, j
                break

    print(f'#{test_case} {BFS(a, b)}')