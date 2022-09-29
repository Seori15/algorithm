# 입력값 설정
for test_case in range(1, 11):
    N = int(input())
    cnt = 0
    arr = list(map(int, input().split()))

# arr의 양 옆에 [0 0]을 추가한 arr2 생성
    arr2 = [0, 0]
    arr2.extend(arr)
    arr2.extend([0, 0])

# 가로 5칸을 기준으로 가운데가 가장 높을 때, 그 다음 높은 값을 제외하여 합계 구하기
    for i in range(N):
        if arr2[i+2] > arr2[i] and arr2[i+2] > arr2[i+1] and arr2[i+2] > arr2[i+3] and arr2[i+2] > arr2[i+4]:
            top = 0
            for j in [arr2[i], arr2[i+1], arr2[i+3], arr2[i+4]]:
                if j > top:
                    top = j
            cnt += arr2[i+2] - top
    print(f'#{test_case} {cnt}')