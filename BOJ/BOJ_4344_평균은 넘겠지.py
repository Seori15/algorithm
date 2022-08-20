# 평균을 넘은 비율을 소수 셋째점까지 출력하기
C = int(input())
for test_case in range(C):
    arr = list(map(int, input().split()))
    N = arr[0]
    scores = arr[1::]
    bumsaeng = 0
    for i in scores:
        if i > sum(scores) / N:
            bumsaeng += 1

    print(f'{bumsaeng / N * 100:.3f}%')
