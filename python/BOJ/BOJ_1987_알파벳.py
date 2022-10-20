# [A] delta 방향 설정
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# [B] DFS 함수 설정
def dfs(i, j, n):
    global result
    for di, dj in delta:
        ni, nj = i+di, j+dj
        if 0 <= ni < R and 0 <= nj < C and not visited[ord(arr[ni][nj]) - 65]:
            visited[ord(arr[ni][nj])-65] = 1
            dfs(ni, nj, n+1)
            visited[ord(arr[ni][nj])-65] = 0

    if result < n:
        result = n
        return
    else:
        return


# [1] 입력값 설정
R, C = map(int, input().split())
arr = [[] for _ in '_'*R]
for i in range(R):
    arr[i] = list(input().rstrip())

visited = [0]*26
visited[ord(arr[0][0])-65] = 1
result = 0
dfs(0, 0, 1)

print(result)
