# 입력값 설정
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    # 2중 for문으로 각 집의 좌표를 받는다.
    houses = []
    for i in range(N):
        arr = list(map(int, input().split()))
        for j in range(N):
            if arr[j] == 1:
                houses.append([i, j])

    # (0,0)부터 돌면서 distance에 각 집까지 거리를 담는다.
    # K를 줄여가면서 가능한 최대 집 개수를 구한다.
    house = 0
    for i in range(N):
        for j in range(N):
            distance = []
            for a, b in houses:
                distance += [abs(i - a) + abs(j - b)]

            while len(distance) != 0:
                K = max(distance)
                cost = K * K + (K + 1) * (K + 1)
                if M * len(distance) >= cost:
                    if house < len(distance):
                        house = len(distance)
                    break
                else:
                    for n in range(distance.count(K)):
                        distance.remove(K)

    print(f'#{test_case} {house}')
