# 입력값 설정
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    heap = [0]

    # nums에서 1개씩 뽑아서 heap에 추가한다.
    while len(nums) != 0:
        heap.append(nums.pop(0))

        # heap에 추가된 원소 c를 그 부모 p 와 비교하여 배치한다.
        c = len(heap)-1
        while len(heap) > 2:
            p = c // 2
            if heap[p] > heap[c]:
                heap[p], heap[c] = heap[c], heap[p]
                c = c // 2
            else:
                break

    # 마지막 노드 heap[N]의 부모 노드들을 더한다.
    result = 0
    while N != 0:
        N = N // 2
        result += heap[N]
    print(f'#{test_case} {result}')