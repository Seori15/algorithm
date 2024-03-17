def solution(dates):
		# [1] 영희가 좋아하는 숫자를 likes에 담아놓는다.
    likes = ["1", "2", "4", "8"]
    answer = 0
    
    # [2] date에서 /를 제거하고, 날짜의 각 자리수가 likes에 속하는지 판단한다.
    for date in dates:
        days = date.replace("/", "")
        for day in days:
            if day not in likes:
                break
        else: 
            answer += 1

    return answer