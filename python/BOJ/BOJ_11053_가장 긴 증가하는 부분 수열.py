# [1] 입력값 설정
N = int(input())
A = list(map(int, input().split()))

# [2] 수열의 각 i 위치에서 j와 비교할 때, i의 숫자가 크다면 check[i]를 비교 및 갱신한다.
check = [1]*N
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            check[i] = max(check[i], check[j]+1)

print(max(check))