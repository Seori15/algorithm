# 모든 부분 집합을 만드는 풀이 방법
T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    P = []
    result = 0

    for i in range(1<<12):
        temp = []
        for j in range(12):
            if i & (1<<j):
                temp.append(A[j])
        P.append(temp)

# 길이가 N이고 합이 K인 부분집합을 count
    for i in range(len(P)):
        if len(P[i]) == N:
            sum = 0
            for j in P[i]:
                sum += j

            if sum == K:
                result += 1

    print(f'#{test_case} {result}')
