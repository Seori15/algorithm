# [1] 입력값 설정
N = int(input())

# [2] DP 풀이
DP = [0]*(N+1)
for i in range(2, N+1):
    # [2-1] 문제의 3가지 연산을 역순으로 거슬러가며 연산횟수+1한다.
    # 2나 3의 배수일 때는 min값으로 갱신할 수 있도록 한다.
    DP[i] = DP[i-1] + 1
    if i%2 == 0:
        DP[i] = min(DP[i], DP[i//2]+1)
    if i%3 == 0:
        DP[i] = min(DP[i], DP[i//3]+1)
print(DP[N])