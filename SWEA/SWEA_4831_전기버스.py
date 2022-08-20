T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split()) # 1 <= K,N,M <= 100
    charging_stop = list(map(int, input().split()))
    bus = K #마지막 충전위치
    cnt = 0 # 충전횟수
    gap = 0 # 간격이 K넘어갈 때 계산용
    while True:
        if bus >= N:
            break
        elif gap >= K:
            cnt = 0
            break
        elif bus in charging_stop:
            cnt += 1
            bus += K
            gap = 0
        else:
            bus -= 1
            gap += 1

    print(f'#{tc+1} {cnt}')