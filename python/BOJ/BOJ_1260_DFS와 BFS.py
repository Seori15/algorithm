# DFS함수 정의. A에서 시작해서 lines[A] 내 원소 B를 탐색
def DFS(A):
    result_D.append(A)
    visited_D[A] = 1

    for B in sorted(lines[A]):
        if not visited_D[B]:
            DFS(B)

# BFS함수 정의. A에서 시작해서 lines[A] 내 원소 B를 탐색
def BFS(A):
    queue = []
    if not visited_B[A]:
        queue.append(A)
        result_B.append(A)
        visited_B[A] = 1

    # DFS와의 차이를 위해 queue 활용
    while queue:
        n = queue.pop(0)
        for B in sorted(lines[n]):
            if not visited_B[B]:
                result_B.append(B)
                queue.append(B)
                visited_B[B] = 1

# 입력값 설정
N, M, V = map(int, input().split())
lines = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    lines[a].append(b)
    lines[b].append(a)

visited_D = [0] * (N+1)
visited_B = [0] * (N+1)
result_D = []
result_B = []

DFS(V)
print(*result_D)
BFS(V)
print(*result_B)