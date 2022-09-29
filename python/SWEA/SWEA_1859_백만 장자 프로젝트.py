# (a, b) 범위에서 최대값을 구해서, (a, maxI) 범위 최대 이익값 함수
def max_benefit(a, b):
    if a == b:
        return False

    global result
    max_price = 0
    maxI = 0
    for i in range(a, b):
        if max_price < price[i]:
            max_price = price[i]
            maxI = i

    for i in range(a, maxI):
        result += price[maxI] - price[i]

    if maxI != b:
        max_benefit(maxI+1, b)

# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    result = 0
    max_benefit(0, N)
    print(f'#{test_case} {result}')
