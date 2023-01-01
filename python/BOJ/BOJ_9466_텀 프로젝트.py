# [A] match 함수 설정
#     match 함수는 같은 팀 후보를 줄세우면서 머리와 꼬리가 같은지 체크한 뒤 팀원의 수를 반환한다.
def match(n):
    candidate = [n]
    while True:
        now = candidate[-1]
        next = pick[now]

        # [A-1] next 후보가 check가 아니라면 candidate에 추가하고 check처리
        if not check[next]:
            check[next] = 1
            candidate.append(next)

        # [A-2] next 후보가 check 되어있다면, candidate에 추가하고 비교를 시작한다.
        else:
            candidate.append(next)

            # [A-3] 머리와 꼬리가 같아질 때까지 pop(0)하고, 길이를 반환한다.
            while candidate:
                if candidate[0] == candidate[-1]:
                    return len(candidate) - 1
                else:
                    candidate.pop(0)
            return 0


# [1] 입력값 설정
T = int(input())
for tc in range(T):
    n = int(input())
    pick = [0] + list(map(int, input().split()))

    # [2] 1부터 n까지 match 함수를 적용한다.
    #     match 함수는 팀원의 수를 반환하므로 result에서 값을 빼주면 남은 학생들이 된다.
    result = n
    check = [0] * (n + 1)
    for i in range(1, n + 1):
        if not check[i]:
            check[i] = 1
            result -= match(i)

    print(result)