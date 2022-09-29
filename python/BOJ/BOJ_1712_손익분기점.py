# 입력값 설정
A, B, C = map(int, input().split())

# 팔아도 손해면 -1 출력
if B >= C:
    print(-1)

# 손익 분기점이 될 때까지 반복
else:
    print(A // (C - B) + 1)
