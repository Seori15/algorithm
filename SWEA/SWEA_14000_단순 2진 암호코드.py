# 입력값 설정
T = int(input())
dct = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    # 암호코드 56칸 찾아내기
    for i in range(N):
        st = input()
        if '1' in st:
            st2 = st
            end = len(st)-1
            while st[end] == '0':
                end -= 1

    # 암호를 십진수로 바꾸기
    lst = []
    for i in range(end-55, end+1, 7):
        lst.append(dct[st2[i:i+7]])

    # 검증코드 계산하기
    if ((lst[0] + lst[2] + lst[4] + lst[6])*3 + (lst[1] + lst[3] + lst[5]) + lst[7])%10:
        result = 0
    else:
        result = sum(lst)

    print(f'#{test_case} {result}')