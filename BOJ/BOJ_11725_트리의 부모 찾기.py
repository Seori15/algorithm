# queue 사용 풀이
# 입력값 설정
from sys import stdin
N = int(stdin.readline())

# nodes 리스트에 노드 간의 관계를 전부 저장한다.
nodes = [[] for _ in '_'*(N+1)]
for i in range(N-1):
    A, B = map(int, stdin.readline().split())
    nodes[A] += [B]
    nodes[B] += [A]

# q에 1을 저장하고, pop하면서 트리를 탐색한다.
# 각 ch에 parents인 mom 값을 저장하고 출력한다.
queue = [1]
visited = [0]*(N+1)
parents = [0]*(N+1)
visited[1] = 1
while queue:
    mom = queue.pop(0)
    for ch in nodes[mom]:
        if not visited[ch]:
            visited[ch] = 1
            parents[ch] = mom
            queue.append(ch)

for i in range(2, N+1):
    print(parents[i])