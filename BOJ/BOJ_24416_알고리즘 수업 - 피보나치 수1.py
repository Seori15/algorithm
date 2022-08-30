# 피보나치 재귀함수 구현
def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-2) + Fibonacci(n-1)

# 피보나치 DP 구현
def Fibonacci2(n):
    cnt = 0
    fib = [0, 1, 1]
    if n >= 3:
        for i in range(3, n+1):
            cnt += 1
            fib.append(fib[i-2] + fib[i-1])
    return cnt

# 입력값 설정
import sys
N = int(sys.stdin.readline())
print(Fibonacci(N), Fibonacci2(N))