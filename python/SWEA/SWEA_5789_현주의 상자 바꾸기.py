# 입력값 설정하기
T = int(input())
for test_case in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [0]*N

# L, R값 받아서 설정한 arr에 i값 넣어주기
    for i in range(1, Q+1):
        L, R = map(int, input().split())

        for j in range(L-1, R):
            arr[j] = i

    arr = map(str, arr)
    print(f'#{test_case} {" ".join(arr)}')


# 보충수업
# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N, Q = map(int, input().split())

    # 길이 N만큼의 boxes 리스트 생성 후 입력 받을 때마다 L-R 범위의 숫자를 바꿔줌
    boxes = [0]*(N+1)
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            boxes[j] = i
    boxes.pop(0)

    # 출력
    print(f'#{test_case}', *boxes)