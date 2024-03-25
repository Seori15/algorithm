# 피보나치 수열을 직접 리스트에 적용하고 구간 sum을 통해 답을 구했다.
def solution(a, b):
    first, second = 0, 1
    fibonacci = []
    for i in range(b):
        fibonacci.append(second)
        first, second = second, first + second
    answer = sum(fibonacci[a-1:b])
    return answer