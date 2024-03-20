def solution(gawibawibo):
    영희 = 0
    철수 = 0
    for i in range(len(gawibawibo[0])):
        영, 철 = gawibawibo[0][i], gawibawibo[1][i]
        if 영 - 철 in (-2, -3, 5): # 영희가 이기는 경우
            영희 += 1
        elif 철 - 영 in (-2, -3, 5): # 철수가 이기는 경우
            철수 += 1
    answer = [영희, 철수]
    return answer