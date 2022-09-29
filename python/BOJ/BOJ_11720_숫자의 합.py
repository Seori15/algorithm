# 공백 없는 입력값의 합 출력하기
N = int(input())
s = input()

result = 0
for i in range(N):
    result += int(s[i])

print(result)