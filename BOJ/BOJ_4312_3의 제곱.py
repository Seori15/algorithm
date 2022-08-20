# 입력값 받기(0이 나올 때까지 루프)
while True:
    n = int(input())

# N이 0이면 루프 break
    if n == 0:
        break

# 문제 조건을 맞추기 위하여 n - 1
    n += -1

# 3의 a승 집합인 arr 설정. 입력값 n에 따라 arr의 길이가 달라진다.
    arr = []
    a = 0
    while True:
        arr.append(3 ** a)
        a += 1
        if n < 2 ** a:            # 입력값 n이 부분집합의 갯수 2**a보다 작을 때까지만 루프
            break

# arr의 n번째 부분집합 리스트 P 설정
    P = []
    for i in range(len(arr)):
        if n & (1<<i):
            P.append(arr[i])

# P의 값을 형식에 맞게 출력
    print('{ ', end = '')
    for i in P:
        if i == ' ':
            print('}')
            break
        elif i == P[-1]:
            print(f'{i}', end = ' ')
        else:
            print(f'{i}', end = ', ')
    print('}')