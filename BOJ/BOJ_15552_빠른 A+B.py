# input 대신 sys.stdin.readline 사용하여 시간 줄이기
import sys

T = int(input())
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)