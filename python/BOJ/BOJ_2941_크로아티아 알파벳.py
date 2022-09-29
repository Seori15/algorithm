# 1. 입력값 설정하기
s = input()
Croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 2. 조건 설정하기. Croatian 단어가 있다면 *로 바꿔버림.
for i in Croatian:
    if i in s:
        s = s.replace(i, '*')

print(len(s))