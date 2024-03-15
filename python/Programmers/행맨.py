def solution(word, question):
    answer = []

		# [1] 출제자의 단어 word에서 중복되는 문자를 제외하여 cnt에 담는다.
    cnt = ''
    for letter in word:
        if letter in cnt:
            continue
        cnt += letter

		# [2] cnt가 0이 된다면 성공, 그렇지 않다면 실패이다.
    cnt = len(cnt)
    for letter in question:
        if letter in word:
            answer.append("Yes")
            cnt -= 1
            if cnt == 0:
                answer.append("SUCCESS")
                return answer
        else:
            answer.append("No")
    answer.append("FAIL")
    return answer