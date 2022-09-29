# 후위순회 함수 설정
def postorder(n):
    if n <= N:
        if tree[n] == 0:
            tree[n] = postorder(2*n) + postorder(2*n+1)
            return tree[n]
        else:
            return tree[n]
    else:
        return 0

# 입력값 설정
T = int(input())

for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for _ in '_'*M:
        node, value = map(int, input().split())
        tree[node] = value
    postorder(1)
    print(f'#{test_case} {tree[L]}')