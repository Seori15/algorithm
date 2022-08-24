# BFS함수 정의. A에서 시작해서 lines[A] 내 원소 B를 탐색
def BFS(A):
    global visited
    visited = [0] * (N + 1)
    queue = [A]
    visited[A] = 1

    # DFS와의 차이를 위해 queue 활용
    while queue:
        n = queue.pop(0)
        for B in sorted(lines[n]):
            if not visited[B]:
                queue.append(B)
                visited[B] = visited[n] + 1

# 입력값 설정
N, M = map(int, input().split())
lines = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    lines[a].append(b)
    lines[b].append(a)


# BFS를 1부터 N까지 돌려서 visited의 합이 가장 적은 사람이 정답
result = 100000
resultI = 0
for n in range(1, N+1):
    BFS(n)
    if result > sum(visited):
        result = sum(visited)
        resultI = n

print(resultI)