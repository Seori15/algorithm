# quicksort 함수 설정
def quicksort(arr, start, end):
    # 종료 조건. start index가 end 이상일 때
    if start >= end:
        return

    key = start
    i = start + 1
    j = end

    # i는 오른쪽으로, j는 왼쪽으로 검사 시작
    # arr[key]보다 큰 arr[i]와, 작은 arr[j]의 index를 찾는다.
    while i <= j:
        while i <= j and arr[i] <= arr[key]:
            i += 1
        while i <= j and arr[j] >= arr[key] and j > start:
            j -= 1

        # 위에서 찾은 i와 j는 arr[j] <= arr[key] <= arr[i] 의 관계가 된다.
        # 따라서 정렬 시에도 관계는 j <= key <= i 가 되어야 한다.
        # 현재 상태에서는 key < (i, j) 상태이므로 다음 조건에 따라 교환을 실시한다.

        # 1. i < j 인 경우 key < i < j 이므로 우선 i와 j를 바꿔준다.
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]

        # 2. i > j로 엇갈린 상태이면, key < j < i 이므로 key와 j를 바꾸면 key를 기준으로 정렬이 완료된다.
        elif i > j and key != j:
            arr[key], arr[j] = arr[j], arr[key]

    # 위처럼 key를 기준으로 정렬이 되었으면 (0, j-1) (j-1, N-1) 두 그룹으로 나눠서 정렬을 실시한다.
    quicksort(arr, start, j-1)
    quicksort(arr, j+1, end)

# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quicksort(arr, 0, N-1)
    print(f'#{test_case} {arr[N//2]}')