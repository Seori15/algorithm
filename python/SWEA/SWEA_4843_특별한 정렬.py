# 입력값 설정
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    print(f'#{test_case}', end=' ')

    # max, min값을 차례대로 출력하면서 remove하도록 설정
    for i in range(10):
        max = 0
        min = 100
        for i in range(len(num_list)):
            if max < num_list[i]:
                max = num_list[i]
            if min > num_list[i]:
                min = num_list[i]

        if i % 2:
            print(max, end=' ')
            num_list.remove(max)
        else:
            print(min, end=' ')
            num_list.remove(min)
    print()