# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [[] for _ in '_'*25] # 1 ~ 24
    for _ in '_'*N:
        s, e = map(int, input().split())
        arr[e].append(s)  # arr[끝나는 시간]에 시작 시간을 저장한다.

    # s == e인 경우가 없다고 가정하고 풀이
    result = 0
    recent = 0 # 가장 최근 회의가 끝난 시간
    n = 1
    while n < 25:
        # arr[끝나는 시간]에 값이 저장되어 있을 때
        if arr[n]:
            for start in arr[n]:
                if start >= recent: # 시작시간이 recent 이후라면 작업 가능
                    result += 1
                    recent = n
                    break
        n += 1
    print(f'#{test_case} {result}')