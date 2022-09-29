# 입력값 설정
T = int(input())
for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
    la, lb = 1, 1
    ra, rb = P, P
    ca, cb = int((la + ra) / 2), int((lb + rb) / 2)

    countA = 0
    countB = 0
    result = 0  # 출력을 위한 count와 result 설정

    # A와 B가 각각 이진탐색하며 count + 1
    while ca != Pa:
        countA += 1
        if ca < Pa:
            la = ca
            ca = int((la + ra) / 2)
        else:
            ra = ca
            ca = int((la + ra) / 2)

    while cb != Pb:
        countB += 1
        if cb < Pb:
            lb = cb
            cb = int((lb + rb) / 2)
        else:
            rb = cb
            cb = int((lb + rb) / 2)

    # count가 작은 쪽이 result로 출력
    if countA > countB:
        result = 'B'
    elif countB > countA:
        result = 'A'
    print(f'#{test_case} {result}')
