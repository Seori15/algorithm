# 입력값 설정
N = int(input())
prime_factor = []

# 2부터 N까지 나누어 떨어지는 소인수를 찾으면 prime_factor에 추가하고,
# N은 N//i로 바꾸면서 N이 1이 될 때까지 반복한다.
while N != 1:
    for i in range(2, N+1):
        if N % i == 0:
            prime_factor.append(i)
            N = N // i
            break

prime_factor.sort()
for i in prime_factor:
    print(i)