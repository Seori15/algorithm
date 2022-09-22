# 입력값 설정
from sys import stdin
N = int(stdin.readline())
cards = [0] * N
for i in range(N):
    cards[i] = int(stdin.readline())
cards.sort()

# 정렬 상태에서 가장 작은 2개 값을 더해야 한다.
# cards[i+1]에 cards[i]를 더하고, 정렬한다.
result = 0
for i in range(N - 2):
    result += cards[i] + cards[i+1]
    cards[i+1] += cards[i]

    # sort()함수 사용 시 시간 초과가 발생하므로 임시 정렬을 사용한다.
    # 자리를 찾을때까지 한자리씩 땡기고, 자기 자리에 tmp를 넣는다.
    tmp = cards[i+1]
    j = i+2
    while j < N:
        if tmp > cards[j]:
            cards[j-1] = cards[j]
            j += 1
        else:
            cards[j-1] = tmp
            break
    if j == N:
        cards[j-1] = tmp

# for문에서 작동하지 않는 마지막 덧셈
result += cards[N-2] + cards[N-1]

# 위에 작성한 코드는 N이 1일 때 오답이 발생한다.
if N == 1:
    result = 0

print(result)