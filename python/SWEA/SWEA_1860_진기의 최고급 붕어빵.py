# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    customers = list(map(int, input().split()))
    customers.sort()
    t = 0
    bread = 0
    result = 'Possible'
    while customers:
        customer = customers.pop(0)
        # 첫 손님 올때까지 붕어빵 만들기
        while customer != t:
            t += 1
            if t%M == 0:
                bread += K
        # 손님이 왔는데 빵이 없다면 Impossible
        if bread == 0:
            result = 'Impossible'
            break
        else:
            bread -= 1
    print(f'#{test_case} {result}')