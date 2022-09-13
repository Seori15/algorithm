# DFS 함수 설정
def DFS(start, cnt):
    global sum_cnt
    flag = 0
    for i in tree[start]:
        if not visited[i]:
            visited[i] = 1
            cnt += 1
            DFS(i, cnt)
            cnt -= 1
            flag = 1
    if flag == 0:
        sum_cnt += cnt

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

# DFS 탐색하면서 리프 노드까지의 거리 cnt를 sum_cnt에 더한다.
visited = [0] * (N+1)
visited[1] = 1
sum_cnt = 0
DFS(1, 0)

# sum_cnt가 홀수이면 선공이 이긴다.
if sum_cnt % 2:
    print('Yes')
else:
    print('No')