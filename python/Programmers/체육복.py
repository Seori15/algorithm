def solution(people, limit):
    # [1] 사람들을 몸무게 순으로 정렬시킨다.
    #     보트에는 최대 2명밖에 타지 못하므로 가장 무거운 사람과 가벼운 사람 둘만 비교한다.
    people.sort()
    light, heavy = 0, len(people) - 1

    boat = 0
    while light <= heavy:
        # [2] 두 사람의 합이 limit보다 작거나 같다면 둘 다 탈 수 있다.
        if people[light] + people[heavy] <= limit:
            boat += 1
            light += 1
            heavy -= 1
        # [3] 두 사람의 합이 limit보다 크면 무거운 사람만 탄다.
        else:
            boat += 1
            heavy -= 1

    return boat