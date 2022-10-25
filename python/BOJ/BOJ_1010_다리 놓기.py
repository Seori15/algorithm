# [A] 0부터 30까지 factorial 계산
f = [1]*31
for i in range(2, 31):
    f[i] = i*f[i-1]

# [1] 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    print(f[M]//(f[M-N]*f[N]))

ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# [A] factorial 함수 설정
def factorial(n):
    answer = 1
    for i in range(2, n+1):
        answer *= i

    return answer

# [1] 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    print(factorial(M)//(factorial(M-N)*factorial(N)))