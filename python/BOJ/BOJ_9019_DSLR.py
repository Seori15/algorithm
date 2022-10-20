# [1] 입력값 설정
from collections import deque
from sys import stdin
T = int(stdin.readline())
for test_case in range(1, T+1):
    A, B = map(int, stdin.readline().split())

    # [2] BFS 탐색
    visited = [0]*10000
    visited[A] = 1
    queue = deque([(A, ' ')])
    while queue:
        integer, answer = queue.popleft()
        # [2-1] 종료조건. integer이 B랑 같아지면 answer를 출력
        if integer == B:
            print(answer[1:])
            break

        # [2-2] queue에 DSLR을 각각 추가
        D = (integer*2)%10000
        if not visited[D]:
            visited[D] = 1
            queue.append((D, answer+'D'))

        S = integer-1 if integer != 0 else 9999
        if not visited[S]:
            visited[S] = 1
            queue.append((S, answer+'S'))

        L = (integer%1000)*10 + integer//1000
        if not visited[L]:
            visited[L] = 1
            queue.append((L, answer+'L'))

        R = (integer%10)*1000 + integer//10
        if not visited[R]:
            visited[R] = 1
            queue.append((R, answer+'R'))
