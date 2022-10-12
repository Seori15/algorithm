# [1] 입력값 설정
from sys import stdin
N, M = map(int, stdin.readline().split())

portal = [0]*101
visited = [0]*101
for _ in '_'*(N+M):
    u, v = map(int, stdin.readline().split())
    portal[u] = v

# [2] bfs 탐색
from collections import deque
result = 100
queue = deque([(1, 0)])
while queue:
    now, n = queue.popleft()

    if now == 100:
        result = min(result, n)

    for i in range(6):
        now += 1
        if now <= 100 and portal[now] and not visited[now]:
            visited[now] = 1
            queue.append((portal[now], n+1))

        elif now <= 100 and not visited[now]:
            visited[now] = 1
            queue.append((now, n+1))

print(result)