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

# 보충수업
# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    buses = [tuple(map(int, input().split())) for _ in '_'*N]
    stop = [0]*(5001)
    P = int(input())
    lst_C = [int(input()) for _ in '_'*P]


    # 입력받은 버스 노선에 따라 각 정류장을 지나는 버스 수 +1
    for (A, B) in buses:
        for i in range(A, B+1):
            stop[i] += 1

    # 출력 설정
    print(f'#{test_case}', end=' ')
    for i in lst_C:
        print(stop[i], end=' ')
    print()