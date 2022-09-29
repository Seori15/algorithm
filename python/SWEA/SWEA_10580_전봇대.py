# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lines = []
    cnt = 0

    # 입력받으면서 lines에 저장하는데, 교차할 때마다 cnt + 1
    for _ in '_'*N:
        A, B = map(int, input().split())

        lines.append([A, B])
        for a, b in lines:
            if A < a and B > b:
                cnt += 1
            elif A > a and B < b:
                cnt += 1

    print(f'#{test_case} {cnt}')