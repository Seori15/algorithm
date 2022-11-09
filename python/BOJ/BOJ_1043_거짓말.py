# [A] bfs 함수 설정
from collections import deque
def dfs(detective):
    global result
    queue = deque(detective)

    # bfs 탐색으로 detective와 겹치는 사람들을 visited에 체크
    while queue:
        i = queue.popleft()
        if not visited[i]:
            visited[i] = 1
            for j in range(1, N+1):
                if not visited[j] and adjM[i][j]:
                    queue.append(j)




# [1] 입력값 설정
from sys import stdin
N, M = map(int, stdin.readline().split())

# 진실을 아는 사람들을 detective list로 받는다.
truth = [0]*(N+1)
T, *detective = map(int, stdin.readline().split())


# [2] 각 파티의 참가자들 attendants간의 관계를 adjM에 기록하고,
# attendants들은 다시 쓸 일이 있으므로 parties에 저장한다.
parties = []
adjM = [[0]*(N+1) for _ in '_'*(N+1)]
for _ in '_'*M:
    P, *attendants = map(int, stdin.readline().split())
    parties.append(attendants)
    for i in range(P):
        for j in range(i+1, P):
            adjM[attendants[i]][attendants[j]] = 1
            adjM[attendants[j]][attendants[i]] = 1


# [3] BFS 탐색으로 진짜들을 visited에 담는다.
visited = [0]*(N+1)
dfs(detective)

# [4] [2]의 attendants들을 다시 돌면서, visited와 겹친다면 개수 -1
result = M
for i in range(M):
    for attendant in parties[i]:
        if visited[attendant]:
            result -= 1
            break

print(result)