# [1] 입력값 설정
N, K = map(int, input().split())
DP = [0]*(K+1)

# [2] DP는 1차원 배열이다. 입력을 받을 때마다 DP 배열을 갱신한다.
#     K부터 W까지 역순으로 DP[i](= 현재까지의 최대값)과 V+DP[i-W](= 이번 물건을 포함한 최대값)을 비교한다.
#     이 코드를 정순으로 돌리면 같은 물건을 여러 번 넣게 되어 틀린 답이 나온다.
for _ in '_'*N:
    W, V = map(int, input().split())
    for i in range(K, W-1, -1):
        DP[i] = max(DP[i], V+DP[i-W])

print(DP[K])