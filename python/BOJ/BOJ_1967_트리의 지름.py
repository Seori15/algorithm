from sys import setrecursionlimit
setrecursionlimit(10**9)

# [A] dfs 재귀함수 설정
def dfs(n, d):
    # [A-1] 종료조건. 리프노드라면 total에 가중치를 기록하고 0을 반환
    if tree[n] == []:
        total[n] = d
        return 0

    # [A-2] for문을 돌면서 total에 기록할 largest와 second 값을 찾는다.
    #       next는 자식 노드에서 가장 가중치가 큰 largest 값을 반환한다.
    #       따라서 여기에 n번 노드에서 자식노드까지의 가중치 tree[n][i][1]를 더해준 뒤, 최대값을 비교한다.
    largest, second = 0, 0
    for i in range(len(tree[n])):
        next = dfs(tree[n][i][0], tree[n][i][1]) + tree[n][i][1]
        if next >= largest:
            second, largest = largest, next
        elif second < next < largest:
            second = next

    # [A-3] 찾아낸 최대값 largest와 second를 total에 기록하고 largest를 반환한다.
    total[n] = largest+second
    return largest

# [1] 입력값 설정
n = int(input())
tree = [[] for _ in '_'*(n+1)]
total = [0]*(n+1)
# [1-1] tree 리스트에는 각각 자식 노드와 가중치 정보가 기록된다.
for i in range(n-1):
    p, c, d = map(int, input().split())
    tree[p].append([c, d])

# [2] dfs 재귀를 통해 total[n]에, 노드 n에서 가장 가중치의 합이 큰 largest와 second를 더한 값을 저장한다.
dfs(1, 0)
print(max(total))