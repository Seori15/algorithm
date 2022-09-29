# 입력값 설정
import sys
T = int(sys.stdin.readline())
for test_case in range(1, T+1):
    W, N = map(int, sys.stdin.readline().split())

# 문제 조건 설정
    distance = 0    # 마지막에 출력할 총 이동거리
    trash = 0       # 현재 쓰레기차에 담긴 용량

    # 주어진 곳을 돌면서, 쓰레기 w만큼을 차에 담는다.
    for i in range(N):
        x, w = map(int, sys.stdin.readline().split())
        trash += w

        # 차에 담았을 때 쓰레기의 양이 용량에 도달했다면 쓰레기장에 돌아간다.
        if trash == W:
            distance += 2 * x
            trash = 0
        # 용량을 넘겼다면, 쓰레기장에 갔다와서 다시 쓰레기 w를 싣는다
        elif trash > W:
            distance += 2 * x
            trash = w

        # 마지막 지점이라면 쓰레기장으로 돌아간다.
        # 마지막 지점에서 용량이 꽉 차게 된다면 위의 조건 때문에 2번 계산되므로 조건 반영
        if i == N-1 and trash != 0:
            distance += 2 * x

    print(distance)