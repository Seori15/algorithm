# 시간 출력하기
H, M = map(int, input().split())
if M < 45:
    H, M = H-1, M+15
else:
    M -= 45

if H == -1:
    H = 23

print(H, M)