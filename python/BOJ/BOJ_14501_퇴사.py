# [1] 입력값 설정
from sys import stdin
N = int(stdin.readline())
T = [0]*(N+1)
P = [0]*(N+1)
dp = [0]*(N+2)

for i in range(1, N+1):
    T[i], P[i] = map(int, stdin.readline().split())

# [2] dp 풀이. 마지막날부터 거꾸로 오면서, max(다음날, 오늘 상담을 잡았을 경우 번 총액)
for i in range(N, 0, -1):
    next = i + T[i]
    dp[i] = dp[i+1] if next > N+1 else max(dp[i+1], dp[next]+P[i])

print(dp[1])

---------------------------------
# [A] DFS 함수 설정
def dfs(start, money):
    global result
    # [A-1] 가치지기 조건. N+1일을 넘기면 그대로 종료
    if start > N + 1:
        return
    # [A-2] 종료 조건. N+1일에 도달하면 result값 비교
    elif start == N + 1:
        result = max(result, money)
        return

    dfs(start + T[start], money + P[start]) # 오늘 상담을 잡는 경우
    dfs(start + 1, money) # 오늘 상담을 안 잡는 경우

# [1] 입력값 설정
from sys import stdin

N = int(stdin.readline())
T = [0] * (N + 1)
P = [0] * (N + 1)
for i in range(1, N + 1):
    T[i], P[i] = map(int, stdin.readline().split())

# [2] DFS 탐색
result = 0
dfs(1, 0)
print(result)
