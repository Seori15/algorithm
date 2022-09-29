# 입력값 설정
N = int(input())
numbers = list(map(int, input().split()))

# 소수 리스트 생성. 2부터 1000까지의 수에서 각 수의 배수를 제거해준다.
prime_number = [i for i in range(2, 1001)]
for a in prime_number:
    for b in range(2, 1000//a + 1):
        if a * b in prime_number:
            prime_number.remove(a*b)

# numbers가 소수 리스트에 해당하는 만큼 cnt + 1
cnt = 0
for i in numbers:
    if i in prime_number:
        cnt += 1

print(cnt)


# 또다른 풀이
N = int(input())
numbers = list(map(int, input().split()))
cnt = 0

for i in numbers:
    for j in range(2, i+1):
        if i % j == 0:
            if j == i:
                cnt += 1
            else:
                break

print(cnt)
