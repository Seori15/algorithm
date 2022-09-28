# Runtime Error
# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    visited = [0]*1000001   # 중복처리용 visited
    visited[N] = 1          # 초기값 N 중복처리
    lst = [N]
    idx = 0
    while True:
        a = lst[idx]
        idx += 1

        n = a+1
        if visited[n] == 0 and 0 < n <= 1000000:
            visited[n] = visited[a] + 1
            if n == M:
                break
            lst.append(n)

        n = a-1
        if visited[n] == 0 and 0 < n <= 1000000:
            visited[n] = visited[a] + 1
            if n == M:
                break
            lst.append(n)

        n = a*2
        if visited[n] == 0 and 0 < n <= 1000000:
            visited[n] = visited[a] + 1
            if n == M:
                break
            lst.append(n)

        n = a-10
        if visited[n] == 0 and 0 < n <= 1000000:
            visited[n] = visited[a] + 1
            if n == M:
                break
            lst.append(n)

    print(f'#{test_case} {visited[a]}')



# 109164kb, 3951ms
# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    delta = [1, -1, 0, -10] # 계산용 delta
    visited = [0]*1000001   # 중복처리용 visited
    visited[N] = 1          # 초기값 N 중복처리
    queue = [(N, 0)]
    while queue:
        a, b = queue.pop(0)

        # 1개씩 pop하면서, (계산결과, 연산횟수)를 queue에 저장
        for d in delta:
            if d:
                num = a + d
            else:
                num = a*2
            # 범위 안에 들어오는 수만 저장한다.
            if 0 < num <= 1000000:
                if not visited[num]:
                    visited[num] = 1
                    queue.append((num, b+1))

            if num == M:
                break
        if num == M:
            break

    print(f'#{test_case} {b+1}')