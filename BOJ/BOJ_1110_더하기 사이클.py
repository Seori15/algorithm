# 더하기를 실행한 사이클 길이 출력하기
N = int(input())
N2 = int(N)
cnt = 0
while True:
    a = N2 // 10
    b = N2 % 10
    New = a + b
    c = New % 10
    N2 = 10*b + c
    cnt += 1

    if N == N2:
        break

print(cnt)