# 중위순회 함수 설정
def inorder(n):
    if n <= N:
        inorder(2*n)
        result[n] = tree.pop(0)
        inorder(2*n+1)
    return result

# 입력값 설정
from sys import stdin
T = int(stdin.readline())

for test_case in range(1, T+1):
    N = int(stdin.readline())
    tree = [i for i in range(1, N+1)]
    result = [0]*(N+1)
    inorder(1)
    print(f'#{test_case} {result[1]} {result[int(N/2)]}')