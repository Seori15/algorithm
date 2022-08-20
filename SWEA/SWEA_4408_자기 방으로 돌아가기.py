# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    move = [list(map(int, input().split())) for _ in range(N)]
    rooms = [0]*200

# 각 방의 index를 구해서 rooms[index]를 +1해준다.
    for [a, b] in move:
        if a % 2:
            ai = (a - 1) / 2
        elif a % 2 == 0:
            ai = (a / 2) - 1
        if b % 2:
            bi = (b - 1) / 2
        elif b % 2 == 0:
            bi = (b / 2) - 1

        if ai > bi:
            ai, bi = bi, ai

        ai = int(ai)
        bi = int(bi)
        for i in range(ai, bi+1):
            rooms[i] += 1

# rooms에서 가장 큰 값이 소요 시간이다.
    result = 0
    for i in range(200):
        if result < rooms[i]:
            result = rooms[i]
    print(f'#{test_case} {result}')