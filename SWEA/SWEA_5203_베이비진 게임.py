# 마운틴 인정 룰
# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    cards = list(map(int, input().split()))
    P1, P2 = [0]*10, [0]*10

    # 각자 카드를 2장씩 뽑는다.
    for _ in '_'*2:
        P1[cards.pop(0)] += 1
        P2[cards.pop(0)] += 1

    n = 1
    result = 0
    while n <= 8:
        # 차례에 따라 플레이어가 카드를 가져간다.
        card = cards.pop(0)
        if n%2:
            P1[card] += 1

            if P1[card] == 3: #triplet
                result = 1
                break
            # run
            elif (P1[card%10] and P1[(card-1)%10] and P1[(card+1)%10]) or (P1[card%10] and P1[(card-1)%10] and P1[(card-2)%10]) or (P1[card%10] and P1[(card+1)%10] and P1[(card+2)%10]):
                result = 1
                break
        else:
            P2[card] += 1

            if P2[card] == 3: #triplet
                result = 2
                break
            # run
            elif (P2[card%10] and P2[(card-1)%10] and P2[(card+1)%10]) or (P2[card%10] and P2[(card-1)%10] and P2[(card-2)%10]) or (P2[card%10] and P2[(card+1)%10] and P2[(card+2)%10]):
                result = 2
                break

        n += 1

    print(f'#{test_case} {result}')