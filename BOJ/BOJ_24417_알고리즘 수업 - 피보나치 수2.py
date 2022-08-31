# 피보나치 재귀함수 구현
# arr[n]이 반복 횟수임을 알 수 있음.
def Fibonacci(n):
    for i in range(3, N+1):
        arr[i%3] = arr[(i%3)-2] + arr[(i%3)-1]
        if arr[i%3] >= 1000000007:
            arr[i%3] = arr[i%3] % 1000000007

# 피보나치 DP 구현
# cnt = n-2라는 사실을 알 수 있음.
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
arr = [0, 1, 1]
Fibonacci(N)
print((arr[N%3]), N-2)