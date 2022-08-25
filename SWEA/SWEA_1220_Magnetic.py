# 1. 입력값 설정하기
for test_case in range(1, 11):
    length = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # arr2에 1과 2만 90도 회전하여 입력
    arr2 = [[] for _ in range(100)]
    for j in range(100):
        for i in range(100):
            if arr[i][j]:
                arr2[j].append(arr[i][j])

    # 반복문 while 조건 설정.
    # a. 가장 왼쪽에 2가 온다면 pop(0)
    # b. 가장 오른쪽에 1이 온다면 pop()
    # c. a, b 조건을 거친 후 가장 왼쪽에 1이 온다면, L +1 하고서 2가 나올때까지 pop(0)
    # 전부 pop해서 IndexError가 발생하면 다음 행으로
    L = 0
    n = 0
    while n < 100:
        try:
            if arr2[n][0] == 2:
                arr2[n].pop(0)
            elif arr2[n][-1] == 1:
                arr2[n].pop()

            elif arr2[n][0] == 1:
                arr2[n].pop(0)
                L += 1
                while arr2[n][0] != 2:
                    arr2[n].pop(0)
        except IndexError:
            n += 1

    print(f'#{test_case} {L}')