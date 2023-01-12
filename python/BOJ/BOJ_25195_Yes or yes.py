# [1] 입력값 설정
N, M = map(int, input().split())
adjL = [[] for _ in '_'*(N+1)]
for _ in '_'*M:
    u, v = map(int, input().split())
    adjL[u].append(v)
input()
fans = list(map(int, input().split()))

# [2] 간선 정보가 없는 리프노드를 찾는다.
leaves = []
for i in range(1, N+1):
    if adjL[i] == []:
        leaves.append(i)

# [3] 팬들이 있는 노드는 방문처리한다.
visited = [0]*(N+1)
for fan in fans:
    visited[fan] = 1

# [4] bfs 탐색으로 리프노드까지 도달할 수 있는지 체크한다.
from collections import deque
queue = deque([])
if not visited[1]:
    queue.append(1)
while queue:
    now = queue.popleft()
    if adjL[now] == []:
        print('yes')
        exit()

    for next in adjL[now]:
        if not visited[next]:
            queue.append(next)
print('Yes')