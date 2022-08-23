# 0. 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    S = input().split()
    L = len(S)
    stack = []

# 1. 후위 표기법 계산하기
    operators = ['+', '-', '*', '/']
    for i in range(L):

    # 연산자가 나오면 숫자 2개를 pop해서 계산 후 stack에 추가
        if S[i] in operators:
            try:
                b = stack.pop()
                a = stack.pop()
                if S[i] == '+':
                    stack.append(a + b)
                elif S[i] == '-':
                    stack.append(a - b)
                elif S[i] == '*':
                    stack.append(a * b)
                elif S[i] == '/':
                    stack.append(int(a / b))

            except IndexError:
                break

    # 숫자와 '.'은 stack에 추가
        elif S[i] == '.':
            stack.append(S[i])

        else:
            stack.append(int(S[i]))

# 2. 조건 설정하기
    # 계산이 정상적으로 완료되었을 경우 stack에는 결과값과 . 2개가 있어야 한다.
    result = 0
    if len(stack) != 2:
        result = 'error'
    else:
        result = stack[0]

# 3. 형식에 맞게 출력하기
    print(f'#{test_case} {result}')
