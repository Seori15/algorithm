# 입력값 설정
X = int(input())
N = int(input())

# 구매한 물건의 금액을 sum에 더하는 반복문 설정
sum = 0
for i in range(N):
    a, b = map(int, input().split())
    sum += a * b

# X값이 sum과 같다면 Yes 아니면 No 출력
if X == sum:
    print('Yes')
else:
    print('No')