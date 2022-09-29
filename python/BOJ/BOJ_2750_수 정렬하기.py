# 입력값 설정
N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
for i in arr:
    print(i)