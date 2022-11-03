# [1] 입력값 설정
from sys import stdin
N, M = map(int, stdin.readline().split())
numarr = [[] for _ in '_'*N]
for i in range(N):
    numarr[i] = list(map(int, stdin.readline().split()))
#
# print()
# for i in range(N):
#     print(numarr[i])
# print()

# [1-2] sumarr 2차원 배열에 numarr의 y좌표 구간합을 저장
for i in range(N):
    for j in range(1, N):
        numarr[i][j] += numarr[i][j-1]
for i in range(N):
    for j in range(1, N):
        numarr[j][i] += numarr[j-1][i]

sumarr = [[0]*(N+1) for _ in '_'*(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        sumarr[i][j] = numarr[i-1][j-1]
#
# for i in range(1, N+1):
#     print(sumarr[i])


# [2] 주어진 x, y좌표에 따른 구간합 출력
for _ in '_'*M:
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    print(sumarr[x2][y2] - sumarr[x2][y1-1] - sumarr[x1-1][y2] + sumarr[x1-1][y1-1])
