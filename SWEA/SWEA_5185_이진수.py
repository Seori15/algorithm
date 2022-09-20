# 1. 딕셔너리 풀이
# 16진수 <-> 2진수 dct 생성
dct = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000',
       '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N, st = input().split()

    # 딕셔너리 활용하여 2진수로 변환 후 출력
    result = ''
    for i in st:
        result += dct[i]

    print(f'#{test_case} {result}')

# 2. 2진수 연산 풀이
# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N, num = input().split()
    N = int(N)
    result = ''

    # num 앞에서 차례로 연산. 숫자가 아니라면 아스키 코드 활용
    for i in range(N):
        if num[i].isnumeric():
            tmp = int(num[i])
        else:
            tmp = ord(num[i]) - 55

        # 4자리 2진수이므로 a=8부터 2씩 나누면서 계산
        a = 8
        while a:
            result += str(tmp // a)
            tmp %= a
            a //= 2

    print(f'#{test_case} {result}')

# 3. 2진수 변환 bin함수 풀이
# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N, num = input().split()
    N = int(N)
    result = ''
    for i in range(N):
        tmp = num[i]
        tmp = '0x' + tmp        # 16진수 -> 10진수 변환을 위해 '0x'붙이기
        tmp = int(tmp, 16)      # 10진수로 변환
        tmp = str(bin(tmp)[2:]) # 2진수로 변환하고 앞의 '0b' 떼주기
        while len(tmp) != 4:    # 길이 4 맞춰주기
            tmp = '0' + tmp
        result += tmp
    print(f'#{test_case} {result}')

# 4. 비트 연산 풀이
# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    N, num = input().split()
    N = int(N)
    result = ''

    # num 앞에서 차례로 연산. 숫자가 아니라면 아스키 코드 활용
    for i in range(N):
        if num[i].isnumeric():
            tmp = int(num[i])
        else:
            tmp = ord(num[i]) - 55

        # tmp에 대하여 4자리 비트 AND 연산
        for j in range(3, -1, -1):
            if tmp & (1<<j):
                result += '1'
            else:
                result += '0'

    print(f'#{test_case} {result}')