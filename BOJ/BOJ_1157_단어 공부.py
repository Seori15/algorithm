# 입력값 설정하기
s = input()
arr = [0] * 100

# 소문자인 경우 대문자로 변환
for i in range(len(s)):
    if ord(s[i]) >= 97:
        arr[ord(s[i])-32] += 1
    else:
        arr[ord(s[i])] += 1

# 가장 많이 포함된 알파벳이 여러 종류라면 ? 출력
if arr.count(max(arr)) != 1:
    print('?')

# 가장 많이 포함된 알파벳을 대문자로 출력
else:
    print(chr(arr.index(max(arr))))