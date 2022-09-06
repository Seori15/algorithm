# 입력값 설정
import sys
N = int(sys.stdin.readline())
phones = list(map(int, sys.stdin.readline().split()))

# 반복문 설정
battery = 2         # 총 배터리 소모량. 밑 반복문에서 맨 첫 연결을 뺌
battery_used = 2    # 이번 배터리 소모량
for i in range(1, N):
    # 배터리 소모량이 100을 넘으면 초기화한다.
    if battery >= 100:
        battery = 0
        battery_used = 2

    # 100을 넘지 않았다면 문제 조건 대입. 같은 폰 연결시 2배, 아니면 2퍼
    elif phones[i] == phones[i-1]:
        battery_used *= 2
    else:
        battery_used = 2
    battery += battery_used

# 출력 시 배터리 소모량이 100 이상이라면, 완충된 상태로 출력
if battery >= 100:
    print(0)
else:
    print(battery)