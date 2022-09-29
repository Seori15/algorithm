# 리스트 index 활용 풀이
# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N2 = input()
    N2_lst = list(map(int, N2))
    L2 = len(N2)
    N2 = int(N2, 2)

    N3 = input()
    N3_lst = list(map(int, N3))
    L3 = len(N3)
    N3 = int(N3, 3)

    # 2진수 계산해서 리스트에 넣기
    compare = []
    n = 0
    for i in range(L2-1, 0, -1):
        if N2_lst[i] == 1:
            compare.append(N2 - (2**n))
        else:
            compare.append(N2 + (2**n))
        n += 1

    # 3진수 계산하다가 겹치면 출력하기
    ans = 0
    n = 0
    for i in range(L3-1, -1, -1):
        if i == 0:
            if N3_lst[i] == 1:
                ans = N3 + (3**n)
                if ans in compare:
                    break
            else:
                ans = N3 - (3**n)
                if ans in compare:
                    break

        if N3_lst[i] == 0:
            ans = N3 + (3**n)
            if ans in compare:
                break
            ans = N3 + 2*(3**n)
            if ans in compare:
                break
        elif N3_lst[i] == 1:
            ans = N3 - (3**n)
            if ans in compare:
                break
            ans = N3 + (3**n)
            if ans in compare:
                break
        else:
            ans = N3 - (3**n)
            if ans in compare:
                break
            ans = N3 - 2*(3**n)
            if ans in compare:
                break

        n += 1
    print(f'#{test_case} {ans}')

# str 풀이
# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N2 = input()
    L2 = len(N2)
    N3 = input()
    L3 = len(N3)

    # 2진수 계산해서 compare 리스트에 넣기
    compare = []
    for i in range(L2-1, 0, -1):
        for j in ['0', '1']:
            if N2[i] != j:
                compare.append(int(N2[:i] + j + N2[i+1:], 2))

    # 3진수 계산하다가 겹치면 출력하기
    ans = 0
    for i in range(L3-1, -1, -1):
        if i == 0:
            for j in ['1', '2']:
                if N3[i] != j:
                    if int(N3[:i] + j + N3[i+1:], 3) in compare:
                        ans = int(N3[:i] + j + N3[i+1:], 3)
                        break
            if ans:
                break

        else:
            for j in ['0', '1', '2']:
                if N3[i] != j:
                    if int(N3[:i] + j + N3[i + 1:], 3) in compare:
                        ans = int(N3[:i] + j + N3[i + 1:], 3)
                        break
            if ans:
                break
    print(f'#{test_case} {ans}')