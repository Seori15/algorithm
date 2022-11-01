# [1] 입력값 설정
N, K = map(int, input().split())
tube = [[] for _ in '_'*N]
for i in range(N):
    tube[i] = list(map(int, input().split()))
S, X, Y = map(int, input().split())

# [2] (x, y) 칸을 기준으로 바이러스가 존재하는지를 찾는다.
# [2-1] 설마 만약에 (x, y)에 바이러스가 있다면 출력
x, y = X-1, Y-1
if tube[x][y]:
    print(tube[x][y])

# [2-2] (x, y)부터 거리(n)를 1씩 늘려가면서 바이러스가 있는지를 탐색.
# 바이러스를 발견하면 최솟값을 출력, 끝까지 발견하지 못하면 0을 출력
else:
    virus = []
    for n in range(1, S+1):

        for i in range(x-n, x+n+1):
            for j in range(y-n, y+n+1):
                if 0 <= i < N and 0 <= j < N and abs(x-i) + abs(y-j) == n and tube[i][j]:
                    virus.append(tube[i][j])

        if virus:
            print(min(virus))
            break

    else:
        print(0)
