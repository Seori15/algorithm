# dfs 함수 정의
# graph[v]값을 방문하며 visited[v]를 True로 한다.
def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

# 입력값 설정
while True:
    try:
        T, N = map(int, input().split())
        graph = [[] for _ in range(100)]

# 입력받은 arr의 순서쌍을 a와 b로 분해
        arr = list(map(int, input().split()))
        a = []
        b = []
        for i in range(len(arr)):
            if i % 2:
                b.append(arr[i])
            else:
                a.append(arr[i])

# 빈 graph에 각 노드(a[i])에 연결된 노드(b[i]) 정보를 입력
        for i in range(N):
            graph[a[i]].append(b[i])

        visited = [False] * 100

# 0노드부터 차례차례 dfs 방문하며, visited[99]가 True라면 1을 출력
        dfs(0)

        if visited[99] == True:
            result = 1
        else:
            result = 0
        print(f'#{T} {result}')

    except:
        break