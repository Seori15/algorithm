# [A] delta 방향 설정
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1] # 상하좌우

# [B] dfs 함수 설정
def dfs(i, j, height_now, n, spell):
    global result
    if result < n:
        result = n

    for dr in range(4):
        ni, nj = i+di[dr], j+dj[dr]
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            # [B-1] 다음 칸이 현재 높이보다 낮다면 이동한다.
            if arr[ni][nj] < height_now:
                visited[ni][nj] = 1
                dfs(ni, nj, arr[ni][nj], n+1, spell)
                visited[ni][nj] = 0
            # [B-2] 다음 칸이 현재 높이보다 K 미만만큼 높다면 spell을 사용해서 이동한다.
            elif spell and arr[ni][nj] - K < height_now:
                visited[ni][nj] = 1
                dfs(ni, nj, height_now-1, n+1, 0)
                visited[ni][nj] = 0


# [1] 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [[] for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    maxV = max(map(max, arr))
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == maxV:
                visited = [[0]*N for _ in '_'*N]
                visited[i][j] = 1
                dfs(i, j, maxV, 1, 1)

    print(f'#{test_case} {result}')