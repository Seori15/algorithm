# 입력값 설정
N1, N2 = map(int, input().split())
Group1 = list(input())
Group2 = list(input())
T = int(input())

Group1 = Group1[::-1]

# 개미 속성 부여
G1 = []
G2 = []
for i in range(N1):
    G1.append([Group1[i], 1, i])
for i in range(N2):
    G2.append([Group2[i], 2, i+N1])

# 조건 T에 따라서 개미들이 이동
# T가 1초이면 가운데 2마리가 이동
# T가 2초이면 가운데 4마리가 이동 ...
order = G1+G2
for t in range(1, T+1):
    for i in range(len(order)):
        if order[i][1] == 1 and order[i][2] >= N1-t:
            order[i][2] += 1
        if order[i][1] == 2 and order[i][2] < N1+t:
            order[i][2] -= 1

# 개미 이동 후 정렬
order.sort(lambda x: x[2])
for i in range(N1+N2):
    print(order[i][0], end='')

# order -> [['A', 1, 1], ['L', 1, 3], ['J', 1, 5], ['C', 2, 0], ['R', 2, 2], ['U', 2, 4], ['O', 2, 6]]