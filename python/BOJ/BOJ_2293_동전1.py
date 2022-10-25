# [1] 입력값 설정
n, k = map(int, input().split())
DP = [0]*(k+1)
for i in range(n):
    coin = int(input())
    if coin > k:
        continue

    # [2] DP 풀이. 주어진 동전의 칸에 +1, 이후 값을 더해가며 갱신
    DP[coin] += 1
    for j in range(coin+1, k+1):
        DP[j] += DP[j-coin]

print(DP[k])