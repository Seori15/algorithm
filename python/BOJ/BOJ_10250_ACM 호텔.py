# 입력값 설정
T = int(input())
for test_case in range(T):
    H, W, N = map(int, input().split())

    n = 1
    while N > H:
        n += 1
        N -= H

    print(f'{N*100 + n}')