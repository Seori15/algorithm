# [1] 입력값 설정
n = int(input())
m = int(input())

INF = 100000*n
adjM = [[INF]*(n+1) for _ in '_'*(n+1)]
for _ in '_'*m:
    a, b, c = map(int, input().split())
    adjM[a][b] = min(adjM[a][b], c)
for i in range(1, n+1):
    adjM[i][i] = 0

# [2] 플로이드-와샬 알고리즘
#     i에서 j로 갈 때 k를 거쳐간다고 가정한다.
#     이 경우에 adjM[i][j]와, adjM[i][k] + adjM[k][j]를 비교하여 adjM을 갱신한다.
#     이를 도시의 수만큼 반복한다.
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if adjM[i][j] > adjM[i][k] + adjM[k][j]:
                adjM[i][j] = adjM[i][k] + adjM[k][j]

# [3] 출력값 설정
#     INF값은 0으로 바꿔서 출력한다.
for i in range(1, n+1):
    for j in range(1, n+1):
        if adjM[i][j] == INF:
            adjM[i][j] = 0
    print(*adjM[i][1:])