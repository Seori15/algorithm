# 입력값 설정
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    # max는 0, min은 이론 최대치로 설정
    max_sum = 0
    min_sum = N * 10000

    # num_list에서 M개만큼 더한 i_sum을 각각 max, min값과 비교
    for i in range(N - M + 1):
        i_sum = 0
        for j in range(i, i + M):
            i_sum += num_list[j]
        if i_sum > max_sum:
            max_sum = i_sum
        if i_sum < min_sum:
            min_sum = i_sum
    print(f'#{test_case} {max_sum - min_sum}')