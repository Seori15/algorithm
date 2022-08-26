# 1. 입력값 설정하기
s = input()
l = len(s)
dial = {'ABC':3, 'DEF':4, 'GHI':5, 'JKL':6, 'MNO':7, 'PQRS':8, 'TUV':9, 'WXYZ':10}

# 2. 조건 설정. 입력 단어 s를 순서대로 읽으면서, dial에서 해당하는 번호를 찾아 더한다.
result = 0
for i in range(l):
    for j in dial:
        if s[i] in j:
            result += dial.get(j)
            break
print(result)