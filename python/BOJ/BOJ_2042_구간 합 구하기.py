# [A] 구간 합 트리 생성
def create(start, end, node):
    # [A-1] 완전 이진트리에서 해당 리프 노드에 도달했다면 값을 기록한다.
    if start == end:
        tree[node] = nums[start]
        return tree[node]

    # [A-2] 리프 노드에 도달할 때까지 재귀를 반복하며, 상위 노드에 return값을 기록한다.
    mid = (start + end) // 2
    tree[node] = create(start, mid, node*2) + create(mid+1, end, node*2+1)
    return tree[node]


# [B] 구간 합 구하는 함수
def tree_sum(start, end, node, left, right):
    # [B-1] 구간 합을 구할 left - right 범위가 트리의 start - end 범위 밖에 있다면 0을 반환
    if left > end or right < start:
        return 0
    # [B-2] left - right 범위가 start - end를 완전히 포함한다면 현재 노드 값을 반환
    elif left <= start and end <= right:
        return tree[node]
    # [B-3] left - right 범위가 start - end와 일부만 겹칠 경우, 재귀를 반복하여 return값을 반환
    else:
        mid = (start + end) // 2
        return tree_sum(start, mid, node*2, left, right) + tree_sum(mid+1, end, node*2+1, left, right)

# [C] 원소의 값을 수정하는 함수
def update(start, end, node, index, value):
    # 여기서 index는 처음 받았던 nums 배열의 index를 의미한다.
    # [C-1] index가 트리의 start - end 범위 밖에 있다면 현재 노드 값을 반환
    if index < start or index > end:
        return tree[node]
    # [C-2] index가 해당하는 리프 노드에 도달했다면 값을 value로 수정 및 반환한다.
    if start == end:
        tree[node] = value
        return tree[node]
    # [C-3] 리프 노드에 도달할 때까지 재귀를 반복하여 return 값으로 수정 및 반환한다.
    mid = (start + end) // 2
    tree[node] = update(start, mid, node*2, index, value) + update(mid+1, end, node*2+1, index, value)
    return tree[node]


# 입력값 설정
N, M, K = map(int, input().split())
nums = []
for i in range(N):
    nums.append(int(input()))

# [1] 주어진 nums를 세그먼트 트리로 만들어준다.
tree = [0]*(N*4)
create(0, N-1, 1)

for i in range(M+K):
    # [2] a가 1일 땐 트리의 값을 수정한다.
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, N-1, 1, b-1, c)
    # [3] a가 2일 땐 범위의 구간합을 출력한다.
    elif a == 2:
        print(tree_sum(0, N-1, 1, b-1, c-1))
