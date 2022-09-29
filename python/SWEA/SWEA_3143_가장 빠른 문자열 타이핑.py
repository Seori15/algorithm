# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    A, B = map(list, input().split())
    a, b = len(A), len(B)

# a가 b보다 작을 땐 a를 출력
    if a < b:
        result = a

# B가 A에 포함된 횟수를 나타내는 involved
    else:
        involved = 0
        for i in range(a - b + 1):
            if A[i] == B[0]:
                cnt = 0
                for j in range(b):
                    if A[i+j] == B[0+j]:
                        cnt += 1

# 포함되었다면 계산 후 값을 0으로 바꿈
                if cnt == b:
                    involved += 1
                    for j in range(b):
                        A[i+j] = 0

# 총 타이핑 수 = len(A) - len(B) * involved + involved
        result = a - ((b - 1) * involved)
    print(f'#{test_case} {result}')
