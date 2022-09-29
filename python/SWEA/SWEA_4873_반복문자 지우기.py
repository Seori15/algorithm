# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    s = input()
    stack = []

# stack의 길이가 0이면 append
# stack[-1]과 i가 같으면 pop, 아니라면 append
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    result = len(stack)
    print(f'#{test_case} {result}')