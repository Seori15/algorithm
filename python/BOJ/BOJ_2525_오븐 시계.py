# 시간 출력하기
A, B = map(int, input().split())
C = int(input())

B += C
A += B // 60
B = B % 60

if A >= 24:
    A -= 24

print(A, B)