def solution(n):
    answer = 0
    i = 1
    while i <= n:
        if not n % i:
            answer += i
        i += 1
    return answer