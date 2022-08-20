# 입력값 설정
T = int(input())
for test_case in range(1, T+1):
    s = input()
    bar = 0
    result = 0

# 문제 조건 설정
# 1. (( 연속해서 나오면 bar 늘어남
# 2. ()에서 레이저가 bar를 자르므로 result += bar
# 3. )) 연속해서 나오면 bar 줄어듦, result += 1(bar 끝자락)
    for i in range(len(s)-1):
        if s[i] == '(':
            if s[i+1] == '(':
                bar += 1
            else:
                result += bar
        elif s[i] == ')' and s[i+1] == ')':
            result += 1
            bar += -1
    print(f'#{test_case} {result}')
