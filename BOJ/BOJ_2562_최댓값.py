# 최댓값의 index 구하기
max = 0
maxI = 0
for i in range(9):
    n = int(input())
    if max < n:
        max = n
        maxI = i+1

print(max)
print(maxI)