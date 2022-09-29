# 1. 입력값 설정하기
N = int(input())

# 단어를 N번 받는다.
result = 0
for i in range(N):
    banned = []
    words = list(input())

# 2. 조건 설정하기
    # words를 앞에서부터 pop하면서 검증한다.
    # pop한 문자가 연속해서 나온다면 연속 pop하고, banned 리스트에 넣는다.
    # 만약 pop을 계속해서 len이 0이 되면 검증완료. result + 1
    # banned 리스트에 담긴 문자가 나중에 다시 나온다면 그룹 단어가 아니다. break
    while True:
        if len(words) == 0:
            result += 1
            break

        if words[0] not in banned:
            a = words.pop(0)
            banned.append(a)
            while len(words) != 0 and words[0] == a:
                words.pop(0)
        else:
            break

print(result)