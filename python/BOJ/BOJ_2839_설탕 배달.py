# 입력값 설정
N = int(input())
a = N // 5
b = N // 3
result = []

# 반복문 설정. a, b 범위 내 정확하게 합산이 가능한 조합을 찾는다.
for i in range(a + 1):
    for j in range(b + 1):
        if 5*i + 3*j == N:
            result.append(i+j)

# 조합을 찾지 못하면 -1을, 찾으면 min값을 출력한다.
if len(result) == 0:
    print(-1)
else:
    print(min(result))