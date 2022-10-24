# [1] 입력값 설정
N = int(input())
stairs = [0]*(N+1)
for i in range(1, N+1):
    stairs[i] = int(input())

# [2] DP 풀이.
# 1부터 N까지를 의미하는 DP의 길이와, 현재 상태를 0과 1로 나타내는 인자를 갖는다.
# 두 번째 인자가 1인 경우 2칸 연속 밟았다는 의미이다.
DP = [[0]*(N+1) for _ in '_'*(2)]

# [2-1] N이 3 이하일 때는 초기값이 들어간다.
if N == 1:
    print(stairs[1])
elif N == 2:
    print(stairs[1] + stairs[2])
elif N == 3:
    print(max(stairs[1], stairs[2]) + stairs[3])

# [2-2] N이 4 이상일 때부터 점화식을 통한 일반화가 가능해진다.
else:
    DP[0][1] = stairs[1]
    DP[0][2] = stairs[2]
    DP[1][2] = stairs[1] + stairs[2]
    DP[0][3] = DP[0][1] + stairs[3]
    DP[1][3] = DP[0][2] + stairs[3]

    for i in range(4, N+1):
        DP[0][i] = max(DP[0][i-2], DP[1][i-2]) + stairs[i]
        DP[1][i] = DP[0][i-1] + stairs[i]

    print(max(DP[0][N], DP[1][N]))