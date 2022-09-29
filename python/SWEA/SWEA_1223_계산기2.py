# 0. 입력값 설정
for test_case in range(1,11):
    N = int(input())
    S = input()
    stack = []
    S2 = ''

# 1. 후위 표기법으로 변경하기
    for i in range(N):

    # 숫자는 그대로 출력한다
        try:
            int(S[i])
            S2 += S[i]

    # 연산자는 조건 설정이 필요하다. *을 1순위, +을 2순위로 설정한다.
    # stack[-1]에 같거나 큰 순위 연산자가 온다면, stack[-1]에 낮은 순위가 올때까지 출력 후 stack 추가
        except:
            if len(stack) == 0:         # stack이 비어있다면 stack 추가
                stack.append(S[i])
            elif S[i] == '*':           # stack[-1] 순위가 낮다면 stack 추가
                if stack[-1] == '+':
                    stack.append(S[i])
                else:                   # stack[-1]에 낮은 순위가 오도록 출력
                    while True:
                        S2 += stack.pop()
                        if len(stack) == 0 or stack[-1] == '+':
                            stack.append(S[i])
                            break
            elif S[i] == '+':
                while len(stack) != 0:  # +는 최하위 순위이므로 전부 출력
                    S2 += stack.pop()
                stack.append(S[i])

    # 마지막에 stack에 남은 것들을 전부 출력
    while len(stack) != 0:
        S2 += stack.pop()

# 2. 후위 표기법 계산하기
    stack2 = []
    for i in range(N):

    # 숫자는 stack2에 추가
        try:
            stack2.append(int(S2[i]))

    # 연산자가 나오면 숫자 2개를 pop해서 계산 후 stack2에 추가
        except:
            b = stack2.pop()
            a = stack2.pop()
            if S2[i] == '+':
                stack2.append(a + b)
            elif S2[i] == '*':
                stack2.append(a * b)

# 3. 형식에 맞게 출력하기
    print(f'#{test_case} {stack2[0]}')