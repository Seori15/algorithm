# 입력값 설정하기
T = int(input())
for tc in range(T):
    R, S = input().split()

# 앞의 문자부터 R회 반복하여 출력하기
    P = ''
    for i in range(len(S)):
        P += S[i] * int(R)

    print(P)