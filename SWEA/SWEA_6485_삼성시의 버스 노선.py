# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]

    P = int(input())
    bus_stop = [int(input()) for _ in range(P)]

# 버스가 지나는지 여부를 bus_visit에 표시하여 출력
    bus_visit = [0]*5000
    for [a, b] in bus:
        for i in range(a-1, b):
            bus_visit[i] += 1

    print(f'#{test_case}', end = ' ')
    for c in bus_stop:
        print(bus_visit[c-1], end = ' ')
    print()