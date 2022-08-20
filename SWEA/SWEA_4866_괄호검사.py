# 입력값 설정하기
T = int(input())
for test_case in range(1, T+1):
    s = input()
    result = 1

# 여는 괄호는 stack에 넣고, 닫는 괄호가 나오면 검증한다.
    stack = []
    for i in s:
        if i == '{' or i == '(':
            stack += [i]
        elif i == '}':
            if len(stack) != 0 and stack[-1] == '{':
                stack.pop()
            else:
                result = 0
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                result = 0
                break

# 짝이 맞다면 stack이 비어있을 것이므로 result = 1이 된다.
    if len(stack) != 0:
        result = 0
    print(f'#{test_case} {result}')