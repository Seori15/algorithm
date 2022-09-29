# Kruskal 풀이
# find 함수 설정. 노드 a의 부모를 찾는다.
def find(a):
    while parent[a] != a:
        a = parent[a]
    return parent[a]

# union 함수 설정. a와 b 노드를 합친다.
def union(a, b):
    global result
    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

# 입력값 설정
T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())

    # 입력받는 간선과 w 정보를 가중치 순으로 정렬하여 edges에 저장한다.
    edges = [[] for _ in '_'*E]
    for i in range(E):
        edges[i] = tuple(map(int, input().split()))
    edges.sort(key = lambda x:x[2])

    parent = list(range(V+1))
    result = 0
    cnt = 0
    # 가중치 순서대로 union한다. 이 때 a, b의 부모가 같다면 이미 연결된 노드이므로 무시한다.
    # cnt를 세서 모든 노드가 연결되면 break
    for (n1, n2, w) in edges:
        a, b = find(n1), find(n2)
        if a != b:
            union(a, b)
            result += w
            cnt += 1
            if cnt == V:
                break
    print(f'#{test_case} {result}')

------------------------------------------------------
# Prim2 풀이
# prim 함수 설정
def prim(n):
    visited = [0]*(V+1)
    visited[n] = 1
    result = 0

    # 간선을 V개 연결할 때까지 반복한다.
    for _ in '_'*V:
        idx = 0
        minV = 11

        # 0부터 V까지 노드 중에 연결된 노드를 찾는다.
        for i in range(V+1):
            if visited[i] == 1:

                # 연결된 노드 i와 연결되지 않은 노드 j 간의 가중치가 가장 낮은 값을 채택하여 연결한다.
                for j in range(V+1):
                    if visited[j] == 0 and 0 < adjM[i][j] < minV:
                        idx = j
                        minV = adjM[i][j]

        result += minV
        visited[idx] = 1

    return result

# 입력값 설정
T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adjM = [[0]*(V+1) for _ in '_'*(V+1)]

    # 입력받는 간선과 w 정보를 adjM에 저장한다.
    for i in range(E):
        n1, n2, w = map(int, input().split())
        adjM[n1][n2] = w
        adjM[n2][n1] = w

    print(f'#{test_case} {prim(0)}')

------------------------------------------------------
# Prim1 풀이
# prim 함수 설정
def prim(n):
    visited = [0]*(V+1)
    key = [11]*(V+1)
    key[n] = 0         # 시작점의 가중치는 0이다.

    # 간선의 연결 수 V만큼 반복한다.
    for _ in '_'*V:
        i = 0
        minV = 11

        # 0부터 V까지 노드 중에 연결되지 않았고 key가 최소인 노드 i를 찾는다.
        for idx in range(V+1):
            if visited[idx] == 0 and key[idx] < minV:
                i = idx
                minV = key[i]
        visited[i] = 1

        # 연결되지 않은 노드들의 key값을 adjM[i][j]로 갱신한다.
        for j in range(V+1):
            if visited[j] == 0 and adjM[i][j] > 0:
                key[j] = min(key[j], adjM[i][j])

    return sum(key)

# 입력값 설정
T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adjM = [[0]*(V+1) for _ in '_'*(V+1)]

    # 입력받는 간선과 w 정보를 adjM에 저장한다.
    for i in range(E):
        n1, n2, w = map(int, input().split())
        adjM[n1][n2] = w
        adjM[n2][n1] = w

    print(f'#{test_case} {prim(0)}')