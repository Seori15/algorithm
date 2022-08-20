# 입력값 설정하기
T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)

# str1이 str2에 포함되어 있다면 1을, 아니면 0을 출력
    result = 0
    for i in range(M-N+1):
        if str2[i] == str1[0]:
            count = 0
            for j in range(N):
                if str2[i+j] == str1[j]:
                    count += 1
                if count == N:
                    result = 1

    print(f'#{test_case} {result}')