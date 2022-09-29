# 특정 길이마다 줄 바꾸면서 출력하기
T = int(input())
for t in range(1, T+1):

    N = int(input())
    result = ""
    for n in range(1, N+1):
        Ci, Ki = input().split()
        Ki = int(Ki)
        result = result + Ci*Ki
        L = len(result)

    print('#{}'.format(t))
    length = 0
    for i in range(L):
        print(result[i], end="")
        length = length + 1
        if length == 10:
            length = 0
            print()
    print()