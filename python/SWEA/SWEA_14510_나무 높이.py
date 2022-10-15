# 입력값 설정
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))

    height = max(trees)

    odd = 0  # 1 줘야하는 횟수
    even = 0  # 2 줘야하는 횟수
    for tree in trees:
        water = height - tree
        if water % 2:
            odd += 1
        even += water // 2

    # even과 odd의 균형을 맞춰준다.
    while even - odd > 1:
        even -= 1
        odd += 2

    # odd가 크면 odd번만큼 홀수일에 물을 줘야하므로 2*odd - 1
    if odd > even:
        result = odd * 2 - 1
    # even이 크거나 같다면 even번만큼 짝수일에 물을 줘야하므로 2*even
    else:
        result = even * 2
    print(f'#{test_case} {result}')