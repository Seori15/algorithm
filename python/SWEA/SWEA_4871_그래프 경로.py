# dfs 함수 정의
# graph[v]값을 방문하며 visited[v]를 True로 한다.
def dfs(v):

    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

# 빈 graph에 각 노드(a)에 연결된 노드(b) 정보를 입력
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)

    visited = [False] * (V+1)

# S노드부터 차례차례 dfs 방문하며, visited[G]가 True라면 1을 출력
    S, G = map(int, input().split())
    dfs(S)

    if visited[G] == True:
        result = 1
    else:
        result = 0
    print(f'#{test_case} {result}')