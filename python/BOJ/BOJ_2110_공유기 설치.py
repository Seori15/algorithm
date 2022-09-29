# 입력값 설정
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for i in range(N)]
house.sort()

# m과 M은 각각 집 사이 거리의 최소값과 최대값
m, M = 1, house[-1] - house[0]
result = 0

# 집이 2개라면 무조건 처음과 마지막 집에 설치
if C == 2:
    print(M)

# 그 이외에는 distance를 이분탐색하면서 결과값을 찾음
else:
    while(m < M):
        distance = (m + M)//2
        cnt = 1
        router = house[0]   # 마지막 공유기 위치

        # distance 이상의 거리에 집이 있다면 공유기를 설치한다.
        for i in range(N):
            if house[i] - router >= distance:
                cnt += 1
                router = house[i]

        # 설치가 끝났을 때 공유기 개수가 문제 조건 C 이상이라면
        # distance를 늘려가면서 최적의 값을 찾는다.
        # 공유기 개수가 C보다 작다면 distance를 줄여가면서 개수를 맞춘다.
        # 이 때 distance는 이진 탐색 방법으로 결정한다.
        if cnt >= C:
            result = distance
            m = distance + 1
        elif cnt < C:
            M = distance
    print(result)