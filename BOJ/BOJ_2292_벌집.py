# list_k는 점점 더해지는 계차수열 값
list_k = []
k = 0
i = 0
while sum(list_k) <= 1000000000:
    k = 6*i
    list_k.append(k)
    i += 1

# 입력값 설정
N = int(input())

# N-1이 list_k의 합보다 작거나 같을 때, i+1개의 방을 지남.
sum = 0
for i in range(len(list_k)):
    sum += list_k[i]
    if N-1 <= sum:
        print(i+1)
        break
