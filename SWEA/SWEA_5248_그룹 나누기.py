# find 함수 설정
def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

# union 함수 설정
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

# 입력값 설정
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    request = list(map(int, input().split()))

    parent = [i for i in range(N+1)]
    for i in range(M):
        a, b = request[2*i], request[2*i+1]
        union(a, b)

    result = set()
    for i in range(1, N+1):
        result.add(find(i))

    print(f'#{test_case} {len(result)}')