# n이 1이 될 때까지 재귀하며 start, end값을 출력하는 함수 설정
def move(n, start, end, transfer):
    if n == 1:
        print(start, end)
    else:
        move(n-1, start, transfer, end)
        print(start, end)
        move(n-1, transfer, end, start)

# 총 이동 횟수 먼저 출력
def final(N):
    print(2 ** N - 1)
    move(N, 1, 3, 2)

final(int(input()))