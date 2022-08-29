# 함수 설정
def factorial(N):
    if N == 0:
        return 1

    else:
        return N * factorial(N-1)

# 입력값 설정
N = int(input())
print(factorial(N))