# 입력값 설정
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    gogumas = list(map(int, input().split()))

# 조건 설정
    long = 0    # 긴 줄기 수
    cnt = 0
    max_cnt = 0
    result = 0
    maxV = 0
    for i in range(N-1):
        # 오른쪽 구역이 고구마가 많다면, cnt +1한다.
        # cnt가 0이 아니라면 긴 줄기에 포함된다는 의미이다.
        if gogumas[i] < gogumas[i+1]:
            cnt += 1
            result += gogumas[i]

        # cnt가 0이 아니고 오른쪽 구역 고구마가 적다면,
        if cnt != 0 and gogumas[i] > gogumas[i+1]:
            cnt += 1
            result += gogumas[i]
            long += 1
            if max_cnt < cnt:      # cnt와 result를 저장하고 초기화한다
                max_cnt = cnt
                maxV = result
            elif max_cnt == cnt:
                if maxV <= result:
                    maxV = result
            cnt = 0
            result = 0

        # cnt가 0이 아니고 마지막 구역이 더 크다면
        elif cnt != 0 and i == N-2:
            cnt += 1
            result += gogumas[i+1]
            long += 1
            if max_cnt < cnt:      # cnt와 result를 저장한다.
                max_cnt = cnt
                maxV = result
            elif max_cnt == cnt:
                if maxV <= result:
                    maxV = result

    print(f'#{test_case} {long} {maxV}')