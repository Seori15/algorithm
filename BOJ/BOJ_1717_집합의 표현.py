from sys import stdin, setrecursionlimit
setrecursionlimit(10**8)
# find 함수 설정
# 재귀를 통해 합집합의 가장 작은 parent 번호를 불러온다.
def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

# union 함수 설정. a와 b 집합을 합쳐주는 역할을 한다.
# 집합을 합칠 때는 서로 같은 집합에 속한다는 의미로 집합 내 가장 작은 숫자를 parent로 가리키게 된다.
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 입력값 설정
n, m = map(int, stdin.readline().split())
parent = [i for i in range(n+1)]
for i in range(m):
    flag, a, b = map(int, stdin.readline().split())

    # flag가 0일 때는 union 실행
    if not flag:
        union(a, b)
    # flag가 1이면 parent 비교 후 출력
    elif flag:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
