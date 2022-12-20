# [1] 입력값 설정
n = int(input())
lines = list(map(int, input().split()))

# [2] 가장 긴 증가하는 부분 수열
LIS = [0]*(n+1)
for i in range(n):
    idx = lines[i]
    LIS[idx] = max(LIS[:idx])+1 # idx 이전까지의 연속값 중 max값 +1

print(max(LIS))