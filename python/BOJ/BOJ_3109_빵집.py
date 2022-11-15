# [A] dfs 함수 설정
def dfs(i, j):
    # [A-1] 종료 조건. 우측 끝에 도달하면 종료.
    if j == C-1:
        return

    # 가지치기를 위한 변수 possible
    global possible
    possible = 0

    # [A-2] 파이프는 위, 아래, 밑 3방향으로만 설치할 수 있으므로 for문으로 탐색한다.
    for di in range(-1, 2):
        ni, nj = i+di, j+1

        # [A-3] 설치가 가능하면 visited처리하고, 다음 파이프 후보를 찾는다.
        if 0 <= ni < R and arr[ni][nj] == '.' and not visited[ni][nj]:
            possible = 1
            visited[ni][nj] = 1
            dfs(ni, nj)

            # [A-4] 만약 3방향 전부 탐색했는데 설치가 불가능하다면 이전 단계에서 재탐색을 실시해야 한다.
            # 따라서 possible 변수로 다음 단계에서 설치가 가능했는지를 확인하고 return한다.
            if possible:
                return



# [1] 입력값 설정
R, C = map(int, input().split())
arr = [[] for _ in '_'*R]
for i in range(R):
    arr[i] = list(input())

visited = [[0]*C for _ in '_'*R]

# [2] i=0부터 DFS 탐색
for i in range(R):
    dfs(i, 0)

# [3] visited C-1열의 합을 출력
result = 0
for i in range(R):
    result += visited[i][C-1]
print(result)