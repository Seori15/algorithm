T = int(input())
for test_case in range(1, T+1):
    D, A, B, F = map(int, input().split())
    Time = D / (A+B)

    Tf = 0  # 파리 비행시간
    Df = 0  # 파리 비행거리
    Dt = D  # 기차 사이거리
    n = 0
    while Dt > 10**-6:
        n += 1
        if n % 2:
            Tf += Dt / (A+F)
            Df += F * Dt / (A+F)
            Dt = D - ((A+B) * Tf)
        else:
            Tf += Dt / (F+B)
            Df += F * Dt / (F+B)
            Dt = D - ((A+B) * Tf)

    print(f'#{test_case} {Df}')
