# [1] 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [[] for _ in '_'*N]
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    # [2] 구역 설정. (a, b)를 기준으로 section1~4로 나뉨
    result = 100*(N**2)
    for a in range(N-1):
        for b in range(N-1):

            # [2-1] (a, b)의 범위를 바꿔가면서 구역 간의 차이값 탐색
            section1 = 0
            for i in range(a+1):
                for j in range(b+1):
                    section1 += arr[i][j]

            section2 = 0
            for i in range(a+1, N):
                for j in range(b+1):
                    section2 += arr[i][j]

            section3 = 0
            for i in range(a+1):
                for j in range(b+1, N):
                    section3 += arr[i][j]

            section4 = 0
            for i in range(a+1, N):
                for j in range(b+1, N):
                    section4 += arr[i][j]

            diffV = max(section1, section2, section3, section4) - min(section1, section2, section3, section4)

            if result > diffV:
                result = diffV

    print(f'#{test_case} {result}')
