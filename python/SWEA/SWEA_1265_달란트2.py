# 1. 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N, P = map(int, input().split())

    # N/P의 나머지가 존재한다면 remain개만 int(N/P)+1이 되고 나머지는 int(N/P)
    remain = N % P
    if remain:
        result = (int(N/P) ** (P-(remain))) * ((int(N/P)+1) ** (remain))

    # 나머지가 없다면 몫을 P만큼 제곱
    else:
        result = int(N/P) ** P

    print(f'#{test_case} {result}')