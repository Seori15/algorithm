# 입력값 설정하기
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    card = input()

# 카드 수만큼 ai 카운팅하기
    count = [0] * 10
    for i in card:
        count[int(i)] += 1

# count와 index값 출력하기
    index = list(map(int, range(0, 10, 1)))
    M = 0
    for x, y in zip(count, index):
        if x >= M:
            M = x
            Count = x
            Index = y
    print(f'#{test_case} {Index} {Count}')