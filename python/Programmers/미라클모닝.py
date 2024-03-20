def solution(time):
    answer = 0
    for t in time:
        a, b = t.split(" ")
        if b == 'am':
            hour, minute = a.split(":")
            if '03' <= hour < '06':
                answer += 1
            elif hour == '06' and minute <= '30':
                answer += 1
    return answer