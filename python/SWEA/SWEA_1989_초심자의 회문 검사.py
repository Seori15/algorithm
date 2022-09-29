# 단어의 길이를 활용하여 회문 검사하기
N = int(input())
for i in range (1, N+1):
    words = input()
    L = len(words)
    for j in range (0, (L//2)):
        if words[j] == words[L-(j+1)]:
            answer = 1
        else:
            answer = 0
    print("#{} {}".format(i, answer))