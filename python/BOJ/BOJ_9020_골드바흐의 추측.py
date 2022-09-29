# 소수 리스트 prime 생성 - prime[0]부터 배수를 제거하는 방식
prime = [i for i in range(2, 10000)]
for i in prime:
    for j in range(2, 10000//i):
        if (i * j) in prime:
            prime.remove(i * j)

# 입력값 설정
T = int(input())
for test_case in range(T):
    n = int(input())

# x와 n-x가 prime에 존재한다면 print
    for x in range(int(n/2), 0, -1):
        if x in prime and n-x in prime:
            print(x, n-x)
            break