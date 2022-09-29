# 입력받은 만큼 출력하기
import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A+B)
    except:
        break