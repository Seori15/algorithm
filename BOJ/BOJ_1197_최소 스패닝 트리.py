from sys import stdin, setrecursionlimit
setrecursionlimit(10**8)
# 크루스칼 알고리즘 풀이
# find 함수 설정
# 재귀를 통해 합집합의 가장 작은 parent 번호를 불러온다.
def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

# union 함수 설정. a와 b 집합을 합쳐주는 역할을 한다.
# 집합을 합칠 때는 서로 같은 집합에 속한다는 의미로 집합 내 가장 작은 숫자를 parent로 가리키게 된다.
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 입력값 설정
V, E = map(int, stdin.readline().split())
parent = [i for i in range(V+1)]

# 간선과 가중치 정보들을 edges에 저장하고, 가중치 순으로 정렬
edges = [[] for _ in '_'*E]
for i in range(E):
    edges[i] = tuple(map(int, stdin.readline().split()))
edges.sort(key = lambda x:x[2])

# 가중치가 낮은 순으로 노드를 연결한다.
# find(A)와 find(B)가 같다면 이미 연결된 노드이므로 무시한다.
result = 0
for (A, B, C) in edges:
    if find(A) != find(B):
        union(A, B)
        result += C

print(result)

----------------------------------------------------------------

from sys import stdin
# 메모리 초과
# 복습할 겸 프림 알고리즘 풀이
def prim2(r, V):
    MST = [0]*(V+1) # MST에 연결되어 있는지 여부 == visited
    MST[r] = 1      # 시작 노드를 MST 연결 처리
    s = 0           # 반환할 가중치 값

    # MST 특성상 간선을 V-1개 연결하면 완성된다.
    for _ in range(V-1):
        idx = 0
        minV = 2147483648

        # MST에 연결된 노드 i를 찾는다.
        for i in range(1, V+1):
            if MST[i] == 1:
                # 아직 연결되지 않은 노드 중 가장 가중치가 낮은 j를 찾는다.
                for j in range(1, V+1):
                    if adjM[i][j] > 0 and MST[j] == 0 and minV > adjM[i][j]:
                        idx = j
                        minV = adjM[i][j]
        s += minV
        MST[idx] = 1

    return s

# 입력값 설정
V, E = map(int, stdin.readline().split())
adjM = [[0]*(V+1) for _ in '_'*(V+1)]

# adjM 2차원 배열에 가중치 정보를 저장
for i in range(E):
    u, v, w = map(int, stdin.readline().split())
    adjM[u][v] = w
    adjM[v][u] = w

print(prim2(1, V))
