# 입력값 설정
import sys
N, K = map(int, sys.stdin.readline().split())
arr = [0]*N
for i in range(N):
    arr[i] = int(sys.stdin.readline())

# 반복문 설정
M = 0       # 출력할 정수 M
start = 0   # 죽음의 게임 시작점
end = K     # 보성이의 번호
while M < N:
    M += 1

    # 지목해서 보성이의 번호가 나온다면 M을 출력
    if arr[start] == end:
        break

    # 아니라면 보성이가 나올때까지 지목값을 따라감
    else:
        start = arr[start]
        # 계속 돌다가 M이 N이 되어버리면 -1 출력
        if M == N:
            M = -1
            break
print(M)
