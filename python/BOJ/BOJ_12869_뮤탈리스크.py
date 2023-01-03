# [1] 입력값 설정
input()
SCVs = list(map(int, input().split()))
while len(SCVs) != 3:
    SCVs.append(0)

# [2] BFS 방식으로 최소 cnt 탐색.
#     a, b, c가 SCV의 체력이며 max(a, b, c)가 0 이하라면 게임 끝이다.
from collections import deque
queue = deque([sorted(SCVs) + [0]])
while queue:
    a, b, c, cnt = queue.popleft()
    cnt += 1

    # [2-1] 1, 3, 9 순으로 공격하는 경우
    a1, b1, c1 = a-1, b-3, c-9
    if max(a1, b1, c1) > 0:
        queue.append(sorted([a1, b1, c1]) + [cnt])
    else:
        print(cnt)
        break

    # [2-2] 3, 1, 9 순으로 공격하는 경우
    a2, b2, c2 = a-3, b-1, c-9
    if max(a2, b2, c2) > 0:
        queue.append(sorted([a2, b2, c2]) + [cnt])
    else:
        print(cnt)
        break