# BFS 함수 정의. 인접한 병사의 수를 세어준다.
def BFS(i, j, str):
    queue = []
    if not visited[i][j] and arr[i][j] == str:
        queue.append((i, j))
        visited[i][j] = 1
        cnt = 1

        while queue:
            i, j = queue.pop(0)
            for n in direction:
                a, b = i + dx[n], j + dy[n]
                if 0 <= a < M and 0 <= b < N and not visited[a][b] and arr[a][b] == str:
                    queue.append((a, b))
                    visited[a][b] = 1
                    cnt += 1

        # 세었던 병사가 'W'라면 Wlist에, 'B'라면 Blist에 제곱하여 저장
        if str == 'W':
            Wlist.append(cnt**2)
        elif str == 'B':
            Blist.append(cnt**2)

# 입력값 설정
from sys import stdin
N, M = map(int, stdin.readline().split())
arr = [list(stdin.readline()) for _ in '_'*M]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
direction = [0, 1, 2, 3] # 상 하 좌 우
visited = [[0]*N for _ in '_'*M]

# BFS 함수 사용하여 모여있는 병사의 수 제곱 세기
Wlist = []
Blist = []
for i in range(M):
    for j in range(N):
        BFS(i, j, 'W')
        BFS(i, j, 'B')

# 각 리스트의 합 출력
print(sum(Wlist), sum(Blist))
