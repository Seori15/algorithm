def solution(names):
		# [1] 각 이름을 answer에 넣으면서 중복체크를 진행한다. 이후 마지막에 정렬한다.
    answer = []
    for name in names:
        if name not in answer:
            answer.append(name)
    answer.sort()
    return answer