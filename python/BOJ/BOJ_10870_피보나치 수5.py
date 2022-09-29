# 함수 설정
def Fibonacci(N):
    if N == 0:
        return 0

    if N == 1:
        return 1

    else:
        return Fibonacci(N-2) + Fibonacci(N-1)

# 입력값 설정
N = int(input())
print(Fibonacci(N))