# [A] 날짜를 숫자로 바꿔주는 to_number 함수
def to_number(month, day):
    while month != 1:
        month -= 1
        if month in [4, 6, 9, 11]:
            day += 30
        elif month == 2:
            day += 28
        else:
            day += 31

    return day


# [1] 입력값 설정
#     calender[꽃이 피는 날]에 꽃이 지는 날을 to_number 함수를 거쳐 집어넣는다.
calender = [0] * 366
N = int(input())
for _ in '_' * N:
    a, b, c, d = map(int, input().split())
    calender[to_number(a, b)] = max(calender[to_number(a, b)], to_number(c, d))

# [2] 3월 1일 이전에 피는 꽃 선택
maxV = 0
for i in range(1, 61):
    maxV = max(maxV, calender[i])

# [2-1] 선택한 꽃이 3월 전에 져버린다면 조건 불가로 0을 출력.
if maxV <= 60:
    print(0)
    exit()

# [3] 3월 2일부터 조건을 만족하는 꽃 선별. 꽃이 지는 날짜가 11월 30일 이후(335)가 될 때까지 반복
result = 1
now = 60
start = now  # 선택한 꽃이 피는 날짜
end = maxV  # 선택한 꽃이 지는 날짜
while maxV < 335:

    # [3-1] 현재 선택한 꽃이 피고 지는 사이 구간에서 가장 늦게 지는 꽃(maxV)을 선별한다.
    for i in range(start + 1, end + 1):
        if maxV < calender[i]:
            maxV = calender[i]
            now = i

    # [3-2] 위 단계를 거쳐도 maxV가 갱신되지 않았다면 불가능이므로 result = 0 처리
    if end == maxV:
        result = 0
        break

    # [3-3] 새로운 꽃을 선별했으면 result, start, end를 갱신하고 반복한다.
    result += 1
    start = now
    end = maxV

print(result)