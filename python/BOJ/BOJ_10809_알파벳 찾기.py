# 입력값에서 알파벳의 위치 출력하기
S = input()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in alphabet:
    if i in S:
        print(S.find(i), end = ' ')
    else:
        print(-1, end = ' ')