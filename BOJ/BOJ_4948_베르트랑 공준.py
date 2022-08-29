# 소수 판별 리스트 생성
prime_number = [True]*246913
for i in range(2, int(246912**0.5)+1):
    if prime_number[i] == True:
        for j in range(2*i, 246913, i):
            prime_number[j] = False

# 입력값 설정
while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    for i in range(n+1, 2*n+1):
        if prime_number[i] == True:
            cnt += 1

    print(cnt)