# bfs 함수 설정
from collections import deque
def bfs(n):
    visited = [0]*(N+1)
    visited[n] = 1     # 출발점 표시
    queue = deque()
    for (a, b) in MooTube[n]:
        queue.append((a, b))

    # bfs 시작
    result = set()
    while queue:
        start, now = queue.popleft()
        if now >= k: # 현재 USADO(now)가 k 이상이면 result에 담는다.
            result.add(start)

        for (end, USADO) in MooTube[start]: # USADO(now)를 갱신해가면서 queue에 담는다.
            if not visited[end]:
                visited[end] = 1
                new = min(now, USADO)
                queue.append((end, new))

    return len(result)

# 입력값 설정
from sys import stdin
N, Q = map(int, stdin.readline().split())

MooTube = [[] for _ in '_'*(N+1)]
for _ in '_'*(N-1):
    p, q, r = map(int, stdin.readline().split())
    MooTube[p].append((q, r))
    MooTube[q].append((p, r))

# 입력값 v부터 bfs를 실시한다.
for _ in '_'*Q:
    k, v = map(int, stdin.readline().split())
    print(bfs(v))