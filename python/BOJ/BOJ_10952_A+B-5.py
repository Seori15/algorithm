# 0이 입력될 때까지 반복하여 출력하기
import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    if A == 0 and B == 0:
        break
    else:
        print(A+B)