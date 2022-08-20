# 각 자릿수의 합 구하기
N = input()
sum = 0
for i in range (len(N)):
    sum = sum + int(N[i])
print(sum)