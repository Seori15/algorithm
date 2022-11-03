# [1] 입력값 설정
from sys import stdin
N, M = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))

# [1-2] 주어진 nums의 누적합을 nums2에 저장
nums2 = [0]*N
tmp = 0
for i in range(N):
    tmp += nums[i]
    nums2[i] = tmp
nums2 = [0] + nums2

# [2] (i, j) 구간의 구간 합은 nums2에서 nums2[j] - nums2[i-1]과 같다.
for _ in '_'*M:
    i, j = map(int, stdin.readline().split())
    print(nums2[j] - nums2[i-1])