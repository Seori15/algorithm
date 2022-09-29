from itertools import combinations
# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    n = N // 10
    i = 0
    result = 0

# nCi * 2**i 규칙에 따라 계산
    while n >= i:
        arr = [_ for _ in range(n)]
        temp = []
        for j in combinations(arr, i):
            temp.append(j)
        result += len(temp) * (2**i)
        n += -1
        i += 1

    print(f'#{test_case} {result}')