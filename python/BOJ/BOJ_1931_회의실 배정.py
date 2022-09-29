# 입력값 설정하기
N = int(input())
list_meeting = []

for i in range(N):
    x, y = map(int, input().split())
    list_meeting.append((x, y))

# list를 end_time 기준, start_time 기준으로 두 번 정렬
list_meeting.sort(key = lambda x : (x[1], x[0]))

meeting = 0
end_time = 0
for x, y in list_meeting:
    if x >= end_time:
        end_time = y
        meeting += 1
print(meeting)