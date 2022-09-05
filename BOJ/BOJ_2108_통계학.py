# 입력값 설정
import sys
N = int(sys.stdin.readline())

# 최빈값을 위한 count 리스트
count = [0]*8001
arr = []
for i in range(N):
    n = int(sys.stdin.readline())
    arr.append(n)
    count[n+4000] += 1
arr.sort()

# 산술평균
print(round(sum(arr) / N))

# 중앙값
print(arr[N//2])

# 최빈값
num = 0
if count.count(max(count)) == 1:
    print(count.index(max(count))-4000)
else:
    for i in set(arr):
        if arr.count(i) == max(count):
            num += 1
            if num == 2:
                print(i)
                break

# 범위
print(arr[-1] - arr[0])