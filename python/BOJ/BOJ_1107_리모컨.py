# 1. 입력값 설정
N = input()
M = int(input())
if M != 0:
    broken = list((input().split()))
else:
    broken = []

# a값 정의. 현재 채널 100에서 N까지 차이값
a = abs(int(N) - 100)

# b값 정의. 리모콘으로 N 입력 후 가능한 번호 찾기
# case 1. up
U = int(N)
cnt_U = 0
while cnt_U < a:
    for i in str(U):
        if i in broken:
            U += 1
            cnt_U += 1
            break
    else:
        break

# case 2. down
D = int(N)
cnt_D = 0
while cnt_D < a:
    for i in str(D):
        if i in broken:
            D += -1
            cnt_D += 1
            break

    else:
        break
# Up/Down 중 가까운 수를 b로 채택
b = min(cnt_U + len(str(U)), cnt_D + len(str(D)))

# 2. a와 b 비교하여 출력
print(min(a, b))