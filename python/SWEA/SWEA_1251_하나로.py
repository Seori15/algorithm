# dijkstra 함수 설정
def dijkstra(n):
    global result
    distance[n] = 0
    for _ in range(N):

        # distance 값이 가장 작은 i를 고른다.
        minV = INF
        for i in range(N):
            if minV > distance[i] and not visited[i]:
                minV = distance[i]
                ti = i

        # result에 거리를 더하고, 나머지 섬과의 거리를 갱신해준다.
        result += minV
        visited[ti] = 1
        for i in range(N):
            if not visited[i]:
                distance[i] = min(distance[i], ((x[ti]-x[i])**2 + (y[ti]-y[i])**2))

    return round(result*E)

# 입력값 설정
INF = 1000000000000000000

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    x = tuple(map(int, input().split()))
    y = tuple(map(int, input().split()))
    E = float(input())
    distance = [INF]*N
    visited = [0]*N
    result = 0
    print(f'#{test_case} {dijkstra(0)}')