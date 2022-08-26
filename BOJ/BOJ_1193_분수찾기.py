# 1. 입력값 설정
X = int(input())

# 2. 조건 설정. n은 1부터 증가하며, n2는 그 합을 기록한다.
n = 0
n2 = 0

# 반복이 끝났을 때
# n+1 : 2차원배열에서 i와 j 합의 값이 n+1이다
while X > n2:
    n += 1
    n2 += n

if n % 2:
    print(f'{(n2-X)%n+1}/{n-(n2-X)%n}')
else:
    print(f'{n-(n2-X)%n}/{(n2-X)%n+1}')
