# Test_case 수가 정해져있지 않으므로 EOFError 활용
while True:
    try:
        # 입력값 설정
        T = int(input())
        queue = list(map(int, input().split()))

        # 한 숫자가 0이 될 때까지, 5사이클을 반복한다
        while True:
            for i in range(1, 6):
                n = queue.pop(0) - i
                if n <= 0:
                    queue.append(0)
                    break
                queue.append(n)

            if queue[-1] == 0:
                break

        print(f'#{T}', end = ' ')
        print(*queue)

    except EOFError:
        break
