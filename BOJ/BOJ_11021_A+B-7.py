# 형태 맞춰서 T번 출력하기
import sys

T = int(input())
for test_case in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print(f'Case #{test_case}: {A+B}')