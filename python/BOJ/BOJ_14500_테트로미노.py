# 브루트포스 풀이
'''
주어진 테트로미노를 회전, 대칭하여 만들어지는 가지수는 총 19종류이다.
문제에서 주어지는 종이를 2중 for문으로 탐색하면서, 주어진 테트로미노 형태의 숫자 합계를 비교한다.
각 테트로미노당 정사각형 4개로 이루어져 있으므로 i, j가 이동하는 delta를 3개씩 19종류, 총 57개의 delta를 만들어둔다.
본 풀이에서 delta의 순서는 문제에 주어진 도형을 회전/대칭 후 회전 하는 순서대로 설정하였다.
'''
# [A] 테트로미노의 경우의 수에 따른 delta 설정
di = [0, 0, 0, 1, 2, 3, 0, 1, 1, 1, 2, 2, 0, 0, 1, 0, 1, 2, 0, 0, -1, 0, -1, -2, 1, 1, 1, 0, 1, 2, 0, 0, 1, 1, 1, 2, 0, -1, -1, 1, 1, 2, 0, 1, 1, 0, 0, 1, -1, 0, 1, 1, 1, 1, 1, 2, 1]
dj = [1, 2, 3, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 2, 0, 1, 1, 1, 1, 2, 2, 1, 1, 1, 0, 1, 2, 1, 0, 0, 1, 2, 2, 0, 1, 1, 1, 1, 2, 0, -1, -1, 1, 1, 2, 1, 2, 1, 1, 1, 1, -1, 0, 1, 0, 0, 1]
direction = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54]

# [1] 입력값 설정
from sys import stdin
N, M = map(int, stdin.readline().split())
paper = [[] for _ in '_'*N]
for i in range(N):
    paper[i] = list(map(int, stdin.readline().split()))

# [2] 종이에 적혀진 수 탐색 시작
result = 0
for i in range(N):
    for j in range(M):
        for dr in direction:
            sumV = paper[i][j] # dr이 갱신될 때마다 sumV도 초기화된다.

            ni, nj = i+di[dr], j+dj[dr]  # 첫 번째 ni, nj
            if 0 <= ni < N and 0 <= nj < M:
                sumV += paper[ni][nj]

                ni, nj = i+di[dr+1], j+dj[dr+1] # 두 번째 ni, nj
                if 0 <= ni < N and 0 <= nj < M:
                    sumV += paper[ni][nj]

                    ni, nj = i+di[dr+2], j+dj[dr+2] # 마지막 ni, nj
                    if 0 <= ni < N and 0 <= nj < M:
                        sumV += paper[ni][nj]

                        # 총 4개의 수를 더했다면 result값과 비교
                        if result < sumV:
                            result = sumV

print(result)

ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# DFS 풀이
# [A] delta 방향 설정
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1] # 상하좌우

# [B] dfs 함수 설정
def dfs(i, j, n, sumV):
    global result
    # [B-1] 가지치기 조건. 아무리 max를 더해도 result보다 작을 때
    if result > sumV + maxV * (4 - n):
        return
    # [B-2] 종료 조건. 4개의 정사각형을 더했다면 result값과 비교
    if n == 4:
        if result < sumV:
            result = sumV
        return

    # [B-3] 상하좌우 방향대로 bfs 탐색
    for dr in range(4):
        ni, nj = i+di[dr], j+dj[dr]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            if n == 2: # [B-4] 이 조건을 넣지 않으면 'ㅏ' 블럭이 만들어지지 않는다.
                visited[ni][nj] = 1
                dfs(i, j, n+1, sumV + paper[ni][nj])
                visited[ni][nj] = 0

            visited[ni][nj] = 1
            dfs(ni, nj, n+1, sumV + paper[ni][nj])
            visited[ni][nj] = 0

# [1] 입력값 설정
from sys import stdin
N, M = map(int, stdin.readline().split())
paper = [[] for _ in '_'*N]
for i in range(N):
    paper[i] = list(map(int, stdin.readline().split()))

# [2] bfs 탐색
result = 0
maxV = max(map(max, paper))
visited = [[0]*M for _ in '_'*N]
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, paper[i][j])
        visited[i][j] = 0

print(result)