# 인덱스에 유의하여 다음날 주가를 비교한다.
def solution(price):
    answer = 0
    for i in range(len(price)-1):
        if price[i+1] > price[i]:
            answer += 20
        elif price[i+1] < price[i]:
            answer -= 15
    return answer