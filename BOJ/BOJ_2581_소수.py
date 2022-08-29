# 입력값 설정
M = int(input())
N = int(input())
prime = []

# M부터 N까지, 소수이면 prime 리스트에 추가한다.
for i in range(M, N+1):
    for j in range(2, i+1):
        if i % j == 0:
            if j == i:
                prime.append(i)
            else:
                break

# prime 리스트가 비어있다면 -1을, 아니라면 합과 최소값을 출력
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])