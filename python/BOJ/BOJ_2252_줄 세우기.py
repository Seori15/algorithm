# [1] 입력값 설정
N, M = map(int, input().split())
check = [0]*(N+1)
ans = []

# [2] M개 줄에서 주어지는 학생을 a, b라고 했을 때,
#     a는 앞에, b는 뒤에 세우고 check 처리한다.
for _ in '_'*M:
    a, b = map(int, input().split())
    if not check[a]:
        check[a] = 1
        ans = [a] + ans
    if not check[b]:
        check[b] = 1
        ans.append(b)

# [3] 순번을 세우지 않은(check 처리되지 않은) 학생들을 추가한다.
for i in range(1, N+1):
    if not check[i]:
        ans.append(i)

print(*ans)