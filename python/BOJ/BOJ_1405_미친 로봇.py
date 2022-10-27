# [A] delta 방향 설정
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0] # 동서남북

# [B] DFS 함수 설정
def dfs(i, j, cnt, pc):
    global result
    # 가지치기 조건.
    if pc == 0:
        return

    # 종료 조건. 재귀 깊이가 cnt가 n에 달했을 때
    if cnt == n:
        result += pc
        return

    # 범위에 맞게 dfs 탐색
    for dr in range(4):
        ni, nj = i+di[dr], j+dj[dr]
        if -n <= ni <= n and -n <= nj <= n and not visited[ni][nj]:
            visited[ni][nj] = 1
            dfs(ni, nj, cnt+1, pc*percent[dr])
            visited[ni][nj] = 0

# [1] 입력값 설정
n, E, W, S, N = map(int, input().split())
percent = [E/100, W/100, S/100, N/100]

visited = [[0]*(2*n+1) for _ in '_'*(2*n+1)]
visited[0][0] = 1
result = 0
dfs(0, 0, 0, 1)

print(result)