'''
1부터 N//2개까지의 조합을 만들고, 그 조합(comb)과 반대 조합(countercomb)을 bfs 체크한다.
두 선거구가 각자 연결되어 있다면 인구수의 차이를 result에 최솟값으로 갱신한다.
'''
# combination 함수 설정
def combination(arr, n):
    result = []
    if n == 1:
        for i in arr:
            result.append([i])

    else:
        for i in range(len(arr) - (n-1)):
            for j in combination(arr[i+1:], n-1):
                result.append([arr[i]] + j)

    return result

# bfs 함수 설정
def bfs(arr):
    start = arr[0]
    visited = [0]*(N+1)
    visited[start] = 1
    cnt = 0
    queue = [start]
    while queue:
        L = len(queue)
        q2 = []
        for i in range(L):
            s = queue[i]
            cnt += population[s]
            for ss in adjM[s]: # 입력에서 주어진 연결된 구역 정보 중에,
                if not visited[ss] and ss in arr: # 이번 조합에 포함되어 있고 아직 방문체크하지 않았다면 q에 넣기
                    q2.append(ss)
                    visited[ss] = 1
        queue = q2[:]

    return cnt, sum(visited)


# 입력값 설정
from sys import stdin

N = int(stdin.readline())
population = [0] + list(map(int, stdin.readline().split()))
adjM = [[] for _ in '_'*(N+1)]
for i in range(1, N+1):
    n, *arr = map(int, stdin.readline().split())
    adjM[i] = arr

result = sum(population)
for i in range(1, N//2 + 1):
    combs = combination(list(range(1, N+1)), i)
    for comb in combs:
        countercomb = [i for i in range(1, N+1) if i not in comb]
        cnt1, visit1 = bfs(comb)
        cnt2, visit2 = bfs(countercomb)
        if visit1 + visit2 == N:
            result = min(result, abs(cnt1 - cnt2))

# 최소값 갱신이 이루어졌다면 출력하기
if result == sum(population):
    print(-1)
else:
    print(result)