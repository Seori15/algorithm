# 1. 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    # 피자 번호를 포함하는 pizza 리스트 생성
    pizza = []
    for i in range(M):
        pizza.append([i+1, cheese[i]])
    oven = [pizza.pop(0) for _ in range(N)]

# 2. 조건 설정하기
    # 오븐에서 치즈가 다 녹으면 새로운 피자를 투입
    cnt_zero = 0
    while True:
        [a, b] = oven.pop(0)
        b = b // 2
        if b == 0:
            cnt_zero += 1
            if len(pizza) != 0:
                oven.append(pizza.pop(0))
        else:
            oven.append([a, b])

        # M-1개의 치즈가 모두 녹았다면 break
        if cnt_zero == M-1:
            break

    # 마지막에 치즈가 남은 피자의 번호만 출력
    for [a, b] in oven:
        if b != 0:
            result = a

    print(f'#{test_case} {result}')