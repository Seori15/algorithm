# 연속된 문자열 세기
T = int(input())
for test_case in range(T):
    s = input()
    score = 0
    check = 0
    for i in s:
        if i == 'O':
            check += 1
            score += check
        else:
            check = 0

    print(score)
