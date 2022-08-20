# Pascal 함수 정의
def Pascal(N):
    if N == 1:
        return [1]
    if N == 2:
        return [1, 1]
    else:
        lst = [1]
        for i in range(len(Pascal(N-1))-1):
            lst.append(Pascal(N-1)[i] + Pascal(N-1)[i+1])
        lst.append(1)
        return lst

# 입력값 설정, 형식에 맞게 출력
T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    print(f'#{test_case}')
    for i in range(1, N+1):
        print(" ".join(map(str, Pascal(i))))