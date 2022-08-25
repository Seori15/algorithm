# 0. BFS 함수 설정
def BFS(a, b):
    queue = [a]
    visited[a] = 1
    while True:
        n = queue.pop(0)
        for i in lines[n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[n] + 1

        if b in queue:
            return visited[b] -1

        if len(queue) == 0:
            return 0

# 1. 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    V, E = map(int, input().split())
    lines = [[] for _ in range(V+1)]

    for i in range(E):
        a, b = map(int, input().split())
        lines[a].append(b)
        lines[b].append(a)

    S, G = map(int, input().split())
    visited = [0]*(V+1)

    print(f'#{test_case} {BFS(S, G)}')