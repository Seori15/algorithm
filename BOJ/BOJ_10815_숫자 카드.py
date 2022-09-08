# 입력값 설정
import sys
N = int(sys.stdin.readline())
arr = [0]*20000001  # 상근이가 가진 카드를 저장할 배열

cards = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    arr[cards[i]+10000000] += 1     # 카드 숫자를 arr에 저장

M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
for i in range(M):
    if not arr[nums[i]+10000000]:   # arr에 저장되어 있지 않다면 0, 있으면 1
        nums[i] = 0
    else:
        nums[i] = 1
print(*nums)