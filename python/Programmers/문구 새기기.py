# letter의 공백을 replace 함수로 없애고, 남은 길이에 100을 곱한다.
def solution(phrase):
    answer = []
    for letter in phrase:
        answer.append(len(letter.replace(" ", ""))*100)
    return answer