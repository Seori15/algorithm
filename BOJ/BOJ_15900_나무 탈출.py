# DFS 함수 설정
# DFS 함수를 거쳐서 visited에 cnt값을 저장한다.
def DFS(start, cnt):
    visited[start] = cnt

    cnt += 1
    for i in tree[start]:
        if not visited[i]:
            DFS(i, cnt)

# 입력값 설정
import sys
sys.setrecursionlimit(10**5)
N = int(sys.stdin.readline())
tree = [[] for _ in '_'*(N+1)]

# tree에 간선 정보를 입력한다.
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

# print(tree) len 1인게 리프 노드
[[], [8, 4, 3], [3], [1, 2], [1, 7, 6], [6], [4, 5], [4], [1]]

# DFS 탐색하며 정점부터의 거리 cnt를 센다.
visited = [0] * (N + 1)
DFS(1, 1)

# visited에 cnt값이 저장된다.
[0, 1, 3, 2, 2, 4, 3, 3, 2]

# 각 리프 노드에서 cnt 값을 더한다.
cnt = 0
for i in range(2, N+1):
    if len(tree[i]) == 1:
        cnt += (visited[i]-1)

# cnt가 홀수이면 선공이 이긴다.
if cnt % 2:
    print('Yes')
else:
    print('No')
