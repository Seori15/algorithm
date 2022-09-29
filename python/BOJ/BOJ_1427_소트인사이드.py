# 입력값 설정
N = list(map(int, list(input())))

for i in range(len(N)-1, 0, -1):
    for j in range(i-1, -1, -1):
        if N[i] > N[j]:
            N[i], N[j] = N[j], N[i]

for i in N:
    print(i, end = '')