# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())

# N이 1이 될 때까지, 주어진 수로 나누기를 반복
    a, b, c, d, e = 0, 0, 0, 0, 0
    while N != 1:
        if N % 2 == 0:
            N /= 2
            a += 1
        if N % 3 == 0:
            N /= 3
            b += 1
        if N % 5 == 0:
            N /= 5
            c += 1
        if N % 7 == 0:
            N /= 7
            d += 1
        if N % 11 == 0:
            N /= 11
            e += 1
    print(f'#{test_case} {a} {b} {c} {d} {e}')
