# [1] 입력값 설정
N = int(input())
M = int(input())
connecting = [[0]*(N+1)]
for _ in '_'*N:
    connecting.append([0] + list(map(int, input().split())))
visiting = list(map(int, input().split()))

# [2] 첫 도시에서 갈 수 있는 모든 도시를 possible 체크
from collections import deque
start = visiting[0]
possible = [0]*(N+1)
possible[start] = 1
queue = deque([start])
while queue:
    now = queue.popleft()
    for next in range(1, N+1):
        if connecting[now][next]:
            if not possible[next]:
                possible[next] = 1
                queue.append(next)

# [3] 각 도시들이 possible 되어있는지 확인
for city in visiting:
    if not possible[city]:
        print('NO')
        exit()
print('YES')