from sys import stdin
# 입력값 설정
N = int(stdin.readline())
M = int(stdin.readline())
buses = [[] for _ in range(N+1)]
for i in range(M):
    start, end, cost = map(int, stdin.readline().split())
    buses[start].append((start, end, cost))
S, E = map(int, stdin.readline().split())

# 여기서 최소비용 순으로 정렬을 미리 해두어야
# 밑에서 bfs 돌 때 같은 경로를 중복 탐색하는 것을 막을 수 있다.
for i in range(1, N+1):
    buses[i].sort(key = lambda x:x[2])

INF = 100000*N # 버스비 최대값은 도시마다 10만씩 내는 거보다 작음.
key = [INF]*(N+1)
key[S] = 0

# bfs식 풀이. 시작점부터 버스 노선을 탐색하면서, 최솟값을 갱신함.
q = buses[S]
while q:
    q2 = []
    L = len(q)
    for i in range(L):
        start, end, cost = q[i]
        if key[end] > key[start] + cost:
            key[end] = key[start] + cost
            for a, b, c in buses[end]:
                q2.append((a, b, c))
    q = q2[:]

print(key[E])