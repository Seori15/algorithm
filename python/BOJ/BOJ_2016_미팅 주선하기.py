# [1] 입력값 설정
T = int(input())
for test_case in range(T):
    result = 'NO'

    # [2] 각 학생들의 선호도를 조사하여 pick에 담는다.
    pick = [[] for _ in '_' * 11]
    pick[1] = [6, 7, 8, 9, 10]
    for i in range(2, 11):
        pick[i] = list(map(int, input().split()))

    # [3] 솔로가 없어질 때까지 라운드를 계속한다.
    couple = [0] * 6
    solo = [6, 7, 8, 9, 10]
    while solo:
        girl = solo.pop(0)
        boy = pick[girl].pop(0)

        # [4] 고백받은 남학생이 이미 커플인 경우
        if couple[boy]:

            # [정답1] 1번이 두번 이상 고백을 받은 경우 YES가 된다.
            if boy == 1:
                result = 'YES'

            # [4-1] 고백한 여학생의 우선순위가 높을 경우 고백을 받는다.
            if pick[boy].index(couple[boy]) > pick[boy].index(girl):
                solo.append(couple[boy])
                couple[boy] = girl

            # [4-2] 그렇지 않다면 퇴짜놓는다.
            else:
                solo.append(girl)

        # [5] 고백받은 남학생이 솔로라면 고백을 받는다.
        else:
            couple[boy] = girl

    # [정답2] 1번이 6번과 커플이라면 NO가 된다.
    if couple[1] == 6:
        result = 'NO'
    print(result)