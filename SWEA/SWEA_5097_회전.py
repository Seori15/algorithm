# 1. 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))

# 2. 조건 설정
    # queue 맨 앞 숫자를 맨 뒤로 M회 반복
    for i in range(M):
        queue.append(queue.pop(0))

    print(f'#{test_case} {queue[0]}')