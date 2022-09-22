# 입력값 설정
from sys import stdin
T = int(stdin.readline())
for test_case in range(1, T + 1):
    N = int(stdin.readline())

    # applicant[1차성적] = 2차성적 입력
    applicant = [0]*(N+1)
    for _ in '_'*N:
        a, b = map(int, input().split())
        applicant[a] = b

    # 밑 for문에서 i가 커질수록 항상 1차성적 순위가 낮다.
    # 따라서 applicant[i]가 앞에보다 크면 탈락한다.
    alive = N
    start = 1
    for i in range(2, N+1):
        if applicant[i] > applicant[start]:
            alive -= 1
        elif applicant[i] < applicant[start]:
            start = i
    print(alive)