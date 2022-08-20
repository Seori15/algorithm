# 입력값 설정하기
N = int(input())
for test_case in range(1, N+1):
    arr = list(input().split())

# arr의 끝에서부터 출력, pop 반복하며 출력하기
    print(f'Case #{test_case}:', end = ' ')
    for i in range(len(arr)):
        print(arr[-1], end = ' ')
        arr.pop()
    print()