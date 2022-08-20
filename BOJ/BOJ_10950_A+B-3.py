# 입력받은 T번만큼 정수의 합 출력하기
T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print(A + B)