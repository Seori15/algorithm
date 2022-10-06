# bfs 함수 설정
import heapq
def bfs(n):
    key[n] = 0
    heap = []
    heapq.heappush(heap, (0, K))
    # key값이 갱신될 때만 heap에 추가하면서 bfs 탐색
    while heap:
        d, start = heapq.heappop(heap)
        if key[start] < d:
            continue

        for next, d2 in distance[start]:
            dist = d + d2
            if key[next] > dist:
                key[next] = dist
                heapq.heappush(heap, (dist, next))



# 입력값 설정
from sys import stdin
V, E = map(int, stdin.readline().split())
K = int(stdin.readline())

# distance에 각 지역에서 이어진 지역과 거리 저장

distance = [[]*(V+1) for _ in '_'*(V+1)]
for _ in '_'*E:
    u, v, w = map(int, stdin.readline().split())
    distance[u].append((v, w))

INF = 10*V
visited = [0]*(V+1)
key = [INF]*(V+1)
bfs(K)

# 출력 설정
for i in range(1, V+1):
    if key[i] == INF:
        print('INF')
    else:
        print(key[i])