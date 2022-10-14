# [1] 입력값 설정
T = int(input())
result = [0]
for test_case in range(1, T+1):
    A, B, C, D = map(int, input().split())

    # [2] 동시에 켜진 시간은 Off - On
    On = max(A, C)
    Off = min(B, D)
    result.append((Off - On) if (Off - On) > 0 else 0)

for test_case in range(1, T+1):
    print(f'#{test_case} {result[test_case]}')