# 입력값 설정
T = int(input())
for test_case in range(T):
    k = int(input())
    n = int(input())

# apt 조건 설정. 0층에 호수별로 i를 배치
    apt = [[0]*n for _ in range(k+1)]
    apt[0] = [i for i in range(1, n+1)]

# i층 j호는 i-1층의 j호까지의 합
    for i in range(1, k+1):
        for j in range(n):
            for a in range(j+1):
                apt[i][j] += apt[i-1][a]

    print(apt[k][n-1])