# [1] 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    # [2] DP 풀이
    if N == 3:
        print(4)
        continue

    elif N < 3:
        print(N)
        continue
        
    # 1, 2, 3의 합으로 나타내므로 DP[4]부터 규칙성을 보인다.
    # DP[3]까지 초기값을 설정해준다.
    DP = [0]*(N+1)
    DP[1] = 1
    DP[2] = 2
    DP[3] = 4

    # 이후 DP[4]부터는 규칙을 적용한다.
    for i in range(4, N+1):
        DP[i] = DP[i-1] + DP[i-2] + DP[i-3]
    print(DP[N])