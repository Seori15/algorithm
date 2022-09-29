# 입력값 설정
M, N = map(int, input().split())
prime = []

# M부터 N까지 소수이면 prime에 넣고 출력한다.
# 다만 int(i**0.5)+1 조건을 사용할 시 M이 작으면 오작동한다.
# 따라서 remove(1) 구문을 추가해서 보완했다.
for i in range(M, N+1):
    flag = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            flag = False
            break
    if flag == True:
        prime.append(i)

if 1 in prime:
    prime.remove(1)

for i in prime:
    print(i)