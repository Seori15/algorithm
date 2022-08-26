# 1. 입력값 설정
N = int(input())
words = [input().split() for _ in range(N)]
L = list(input().split())

# 2. 조건 설정
# L에서 pop하면서 각 단어가 words[n][-1]에 있는지 찾는다.
# pop 반복하면서 L이 빈다면 Possible, 단어를 찾지 못해서 cnt == N이 되면 Impossible
while True:
    if len(L) == 0:
        print('Possible')
        break

    word = L.pop()
    cnt = 0
    for n in range(N):
        try:
            if words[n][-1] == word:
                words[n].pop()
            else:
                cnt += 1

        except IndexError:
            cnt += 1
            continue

    if cnt == N:
        print('Impossible')
        break
